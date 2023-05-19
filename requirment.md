# Requirements

The following are the requirements for running the "Facial Expressions Recognition with Face Blurring" script:

## Hardware Requirements
- Computer with a webcam or video input device.

## Software Requirements
- Python 3.x
- OpenCV (cv2)
- Mediapipe (mp)
- JSON

## Installation
1. Install Python 3.x: 
   - Download the installer from the official Python website: https://www.python.org/downloads/
   - Follow the installation instructions for your operating system.

2. Install the required Python packages:
   - Open a terminal or command prompt.
   - Run the following commands to install the necessary packages:
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
4. Follow the on-screen prompts and instructions provided by the script.

## Dependencies
The script relies on the following Python packages:
- OpenCV (cv2): A library for computer vision tasks, used for capturing video frames, image processing, and displaying images.
- Mediapipe (mp): A library for building real-time multimedia applications, used for face detection and face mesh processing.
- JSON: A built-in Python module for working with JSON data.

The script assumes that these dependencies are installed and accessible in the Python environment where the script is being executed.

## Supported Platforms
The script should be compatible with the following platforms:
- Windows
- macOS
- Linux

Please note that the availability and compatibility of the dependencies may vary depending on the platform. Ensure that you have the necessary drivers and libraries installed for your operating system.

## Notes
- Make sure you have a webcam connected to your system or adjust the code to use a different video source if needed.
- The script saves the face features to a JSON file with the format "{name}_face_features.json" in the current directory.
- The face blurring effect is applied only during the execution of the script and is not permanently saved in the video stream or image files.
- You can modify the parameters of the face detection, face mesh, and face blurring operations based on your requirements.

Please let me know if you need any further assistance!