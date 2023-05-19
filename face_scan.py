import cv2
import mediapipe as mp
import json
import time

# Initialize the face detection and face mesh modules
mp_face_detection = mp.solutions.face_detection
mp_face_mesh = mp.solutions.face_mesh

# Initialize the video capture
cap = cv2.VideoCapture(0)

# Initialize the face detection and face mesh models
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.8)
face_mesh = mp_face_mesh.FaceMesh()

# Prompt the user for name input
name = input("Enter your name: ")

# Create an empty dictionary to store face features
face_data = {}

# Load existing face data if the file exists
try:
    with open(f"{name}_face_features.json", "r") as json_file:
        face_data = json.load(json_file)
except FileNotFoundError:
    pass

# Process the video frames
start_time = time.time()
while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Convert the image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Perform face detection
    results = face_detection.process(image_rgb)

    # Check for face detections
    if results.detections:
        print("Number of detections:", len(results.detections))

        for detection in results.detections:
            # Get the bounding box coordinates of the face
            bbox = detection.location_data.relative_bounding_box
            h, w, c = image.shape
            x, y, width, height = int(bbox.xmin * w), int(bbox.ymin * h), int(bbox.width * w), int(bbox.height * h)

            # Extract face landmarks using face mesh
            face_results = face_mesh.process(image_rgb)
            if face_results.multi_face_landmarks:
                for face_landmarks in face_results.multi_face_landmarks:
                    # Save face landmarks to face_data dictionary
                    landmarks = [{"x": landmark.x, "y": landmark.y} for landmark in face_landmarks.landmark]
                    if name in face_data:
                        face_data[name].extend(landmarks)
                    else:
                        face_data[name] = landmarks

                    # Draw face landmarks
                    for landmark in face_landmarks.landmark:
                        x_lm, y_lm = int(landmark.x * w), int(landmark.y * h)
                        cv2.circle(image, (x_lm, y_lm), 2, (0, 255, 0), -1)

                    # Blur the face region
                    face_region = image[y:y + height, x:x + width]
                    blurred_face = cv2.GaussianBlur(face_region, (99, 99), 30)
                    image[y:y + height, x:x + width] = blurred_face

    # Display the image
    cv2.imshow('Facial Expressions Recognition with Face Blurring', image)

    if time.time() - start_time >= 5:
        break

    if cv2.waitKey(5) & 0xFF == 27:  # Press Esc to sexit
        break

# Save face features to JSON file
with open(f"{name}_face_features.json", "w") as json_file:
    json.dump(face_data, json_file)
print("the file name is ----- \n\n ")
print(f'{name}_face_fseatures.json')