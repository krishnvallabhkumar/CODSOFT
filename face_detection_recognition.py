import cv2
import os

def detect_faces(image_path):
    face_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(face_cascade_path)

    if face_cascade.empty():
        print("Error: Could not load haar cascade xml file.")
        return

    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not read image at {image_path}")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    print(f"Found {len(faces)} face(s) in the image.")

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(img, "Face Detected", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    output_path = "detected_faces.jpg"
    cv2.imwrite(output_path, img)
    print(f"Result saved to: {os.path.abspath(output_path)}")
    
   

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