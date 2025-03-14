import cv2
from cvzone.HandTrackingModule import HandDetector
import os

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set width
cap.set(4, 720)   # Set height

# Initialize HandDetector
detector = HandDetector(detectionCon=0.7)

# Variables for zoom gesture
startDist = None
scale = 0
cx, cy = 560, 560  # Center coordinates for zoomed image

# Load an image for zooming
image_path = r"./Robo.jpeg"
print(f"Attempting to load image from: {image_path}")
img1 = cv2.imread(image_path)
if img1 is None:
    print("Failed to load image! Please check the file path and ensure the file is accessible.")
    exit()
else:
    print("Image loaded successfully!")

# Resize the image to a smaller size initially
scale_factor = 0.3  # Adjust this value to control the initial size (e.g., 0.5 = 50% of original size)
h1, w1, _ = img1.shape
newH, newW = int(h1 * scale_factor), int(w1 * scale_factor)
img1 = cv2.resize(img1, (newW, newH))
print("Resized image size:", img1.shape[0], img1.shape[1])

while True:
    # Read frame from the webcam
    success, img = cap.read()
    if not success:
        print("Failed to access webcam!")
        break

    # Find hands in the frame
    hands, img = detector.findHands(img)

    # Proceed only if two hands are detected
    if len(hands) == 2:
        # Print finger states for debugging
        fingers1 = detector.fingersUp(hands[0])
        fingers2 = detector.fingersUp(hands[1])
        print("Fingers up (Hand 1):", fingers1)
        print("Fingers up (Hand 2):", fingers2)

        # Check for the zoom gesture (Index and thumb up on both hands)
        if fingers1 == [1, 1, 0, 0, 0] and fingers2 == [1, 1, 0, 0, 0]:
            print("Zoom Gesture Detected")

            # Get landmarks of both hands
            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]

            # Calculate the distance between the centers of both hands
            if startDist is None:
                length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
                startDist = length

            length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
            scale = int((length - startDist) // 2)
            scale = max(-min(h1, w1) // 2, min(scale, min(h1, w1) // 2))  # Clamp scale
            cx, cy = info[4:]
            print("Scale:", scale)

        else:
            startDist = None

        # Apply zoom to the loaded image
        try:
            h1, w1, _ = img1.shape
            newH, newW = ((h1 + scale) // 2) * 2, ((w1 + scale) // 2) * 2
            print("Resized image size:", newH, newW)

            # Resize the image
            img1_resized = cv2.resize(img1, (newW, newH))

            # Overlay the resized image onto the webcam feed
            h, w, _ = img.shape
            top = max(0, cy - newH // 2)
            bottom = min(h, cy + newH // 2)
            left = max(0, cx - newW // 2)
            right = min(w, cx + newW // 2)

            img[top:bottom, left:right] = img1_resized[:bottom-top, :right-left]
        except Exception as e:
            print("Error during resizing or overlay:", e)

    # Display the output
    cv2.imshow("Image", img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
