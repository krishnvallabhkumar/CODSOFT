import os
try:
    from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
    import torch
    from PIL import Image
except ImportError:
    print("Missing required libraries. Please run: pip install transformers torch torchvision pillow")
    exit()

model_name = "nlpconnect/vit-gpt2-image-captioning"
model = VisionEncoderDecoderModel.from_pretrained(model_name)
feature_extractor = ViTImageProcessor.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def predict_step(image_paths):
    images = []
    for image_path in image_paths:
        i_image = Image.open(image_path)
        if i_image.mode != "RGB":
            i_image = i_image.convert(mode="RGB")
        images.append(i_image)

    pixel_values = feature_extractor(images=images, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)

    gen_kwargs = {"max_length": 16, "num_beams": 4}
    output_ids = model.generate(pixel_values, **gen_kwargs)

    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]
    return preds

def main():
    print("--- Image Captioning AI ---")
    print(f"Using device: {device}")
    
    image_path = input("Enter the full path to an image file (e.g., image.jpg): ").strip()
    
    if os.path.exists(image_path):
        print("Generating caption... (This may take a moment on first run)")
        try:
            captions = predict_step([image_path])
            print(f"\nCaption: {captions[0]}")
        except Exception as e:
            print(f"Error processing image: {e}")
    else:
        print("File not found. Please provide a valid path.")

if __name__ == "__main__":
    main()