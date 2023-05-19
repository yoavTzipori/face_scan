# Facial Expressions Recognition with Face Blurring

This code is a Python script that performs facial expressions recognition and face blurring using the Mediapipe library. It utilizes computer vision techniques to detect faces in a live video stream, extract facial landmarks, and apply various operations on the detected face regions.

## Prerequisites
Before running the code, ensure that you have the following dependencies installed:
- OpenCV (cv2)
- Mediapipe (mp)
- JSON

You can install these dependencies using pip:
```
pip install opencv-python
pip install mediapipe
```

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script using the following command:
   ```
   python script.py
   ```
4. The program will prompt you to enter your name. Please enter your name and press Enter.

## Functionality
1. The script initializes the face detection and face mesh modules provided by Mediapipe.
2. It initializes the video capture, which captures frames from the default camera (index 0).
3. The face detection and face mesh models are loaded.
4. The program creates an empty dictionary to store face features.
5. If face feature data for the entered name exists, it is loaded from the corresponding JSON file.
6. The script starts processing video frames in a loop.
7. For each frame, it performs the following steps:
   - Converts the image to RGB format.
   - Performs face detection using the loaded face detection model.
   - If faces are detected, it prints the number of detections and proceeds with face mesh processing.
   - For each face, it extracts facial landmarks using the face mesh model and saves them to the face_data dictionary.
   - It draws the face landmarks on the image.
   - Blurs the face region using Gaussian blur.
   - Displays the processed image with facial landmarks and face blurring.
   - If five seconds have elapsed since the start of the program, the loop exits.
   - If the Esc key is pressed, the loop exits.
8. The script saves the face feature data to a JSON file named "{name}_face_features.json".
9. It prints the name of the generated JSON file.

## Notes
- Make sure you have a webcam connected to your system or adjust the code to use a different video source if needed.
- The script saves the face features to a JSON file with the format "{name}_face_features.json" in the current directory.
- The face blurring effect is applied only during the execution of the script and is not permanently saved in the video stream or image files.
- You can modify the parameters of the face detection, face mesh, and face blurring operations based on your requirements.

Please let me know if you need any further assistance!