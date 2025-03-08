import cv2
from cvzone.HandTrackingModule import HandDetector

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
img1 = cv2.imread(r"Img path")
if img1 is None:
    print("Image not found! Please check the file path.")
    exit()

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

            # Update scale based on the distance between hands
            length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
            scale = int((length - startDist) // 2)
            cx, cy = info[4:]
            print("Scale:", scale)

        else:
            startDist = None

        # Apply zoom to the loaded image
        try:
            h1, w1, _ = img1.shape
            print("Original image size:", h1, w1)

            newH, newW = ((h1 + scale) // 2) * 2, ((w1 + scale) // 2) * 2
            print("Resized image size:", newH, newW)

            # Resize the image
            img1_resized = cv2.resize(img1, (newW, newH))

            # Overlay the resized image onto the webcam feed
            img[cy - newH // 2:cy + newH // 2, cx - newW // 2:cx + newW // 2] = img1_resized
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
