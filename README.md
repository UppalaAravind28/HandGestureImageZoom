---

# Hand Gesture Image Zoom

A Python-based real-time hand gesture-controlled image zoom application using OpenCV and cvzone. This project allows you to dynamically zoom in or out of an image by using two-hand gestures detected via a webcam.

---

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Configuration](#configuration)
6. [Troubleshooting](#troubleshooting)
7. [Contributing](#contributing)
8. [License](#license)
9. [Acknowledgments](#acknowledgments)

---

## Features
- Real-time hand detection using Mediapipe
- Zoom in/out using two-hand gestures (index finger and thumb raised)
- Dynamic image resizing based on the distance between hands
- Webcam integration for seamless interaction
- Customizable image overlay for personalization

---

## Requirements
- Python 3.6 or higher
- A working webcam
- The following Python libraries:
  - `opencv-python`
  - `cvzone`
  - `mediapipe`

---

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/hand-gesture-zoom.git
   cd hand-gesture-zoom
   ```

2. **Install dependencies**:
   Install the required Python packages using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your image**:
   Place the image you want to zoom in the project directory (e.g., `Robo.jpg`) and update the script if needed:
   ```python
   img1 = cv2.imread("Robo.jpg")  
   ```

---

## Usage
1. **Run the script**:
   Execute the main script using Python:
   ```bash
   python main.py 
   ```

2. **Controls**:
   - Show **two hands** with **index finger and thumb raised** to activate zoom.
   - Move hands **closer together** to zoom out.
   - Move hands **farther apart** to zoom in.
   - Press **`q`** to quit the application.

---

## Configuration
You can customize the application by modifying the following parameters in the script:

- **Webcam resolution**:
  Adjust the resolution of the webcam feed:
  ```python
  cap.set(3, 1280)  # Width
  cap.set(4, 720)   # Height
  ```

- **Hand detection sensitivity**:
  Change the detection confidence threshold:
  ```python
  detector = HandDetector(detectionCon=0.7)  # Adjust `detectionCon` (0.1 to 1.0)
  ```

- **Image path**:
  Update the path to your desired image:
  ```python
  img1 = cv2.imread("path/to/your/image.jpg")
  ```

---

## Troubleshooting
- **Image not loading**:
  - Ensure the image exists in the specified path.
  - Use a relative path (e.g., `"Robo.jpg"`) or provide the absolute path.

- **Webcam not detected**:
  - Ensure no other applications are using the webcam.
  - Test the webcam with a simple script:
    ```python
    import cv2
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        cv2.imshow("Test", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    ```

- **Dependencies not installed**:
  - Run `pip install -r requirements.txt` to install all required packages.

---

## Contributing
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- [OpenCV](https://opencv.org/) for computer vision tools
- [cvzone](https://github.com/cvzone/cvzone) for hand tracking
- [Mediapipe](https://mediapipe.dev/) for hand landmark detection

---

### Directory Structure
```
hand-gesture-zoom/
├── main.py            # Main script
├── requirements.txt   # Dependencies
├── Robo.jpg           # Example image (replace with your own)
├── README.md          # Documentation
└── LICENSE            # License file
```

---
