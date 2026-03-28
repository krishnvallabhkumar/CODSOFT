import cv2
import os

def detect_faces(image_path):
    # Load the pre-trained Haar Cascade classifier for face detection
    # This file is usually included with opencv installation
    face_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(face_cascade_path)

    if face_cascade.empty():
        print("Error: Could not load haar cascade xml file.")
        return

    # Read the input image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not read image at {image_path}")
        return

    # Convert the image to grayscale (required for Haar Cascades)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    # scaleFactor: How much the image size is reduced at each image scale
    # minNeighbors: How many neighbors each candidate rectangle should have to retain it
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    print(f"Found {len(faces)} face(s) in the image.")

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Add a label for 'Recognition' placeholder
        cv2.putText(img, "Face Detected", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Save or display the result
    output_path = "detected_faces.jpg"
    cv2.imwrite(output_path, img)
    print(f"Result saved to: {os.path.abspath(output_path)}")
    
    # Note on Recognition:
    # For actual face recognition (identifying WHO it is), you would typically:
    # 1. Crop the face: face_img = gray[y:y+h, x:x+w]
    # 2. Compare it to known faces using a library like 'face_recognition' (based on dlib)
    #    or use a Siamese Network (like VGGFace or FaceNet) to get embeddings.

def main():
    print("--- Face Detection & Recognition AI ---")
    print("Note: This script uses Haar Cascades for efficient face detection.")
    
    image_path = input("Enter the full path to an image file (e.g., photo.jpg): ").strip()
    
    if os.path.exists(image_path):
        detect_faces(image_path)
    else:
        print("File not found. Please provide a valid path.")

if __name__ == "__main__":
    # Ensure opencv-python is installed
    try:
        main()
    except ImportError:
        print("Error: 'opencv-python' is not installed. Please run: pip install opencv-python")
