import cv2
from pyzbar.pyzbar import decode

# Open a video capture object (use 0 for default camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Decode QR codes and barcodes from the frame
    decoded_objects = decode(gray_frame)

    for obj in decoded_objects:
        # Extract the barcode or QR code data
        data = obj.data.decode('utf-8')

        # Draw a bounding box around the detected object
        points = obj.polygon
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            cv2.polylines(frame, [hull], True, (0, 255, 0), 2)
        else:
            for j in range(4):
                cv2.line(frame, tuple(points[j]), tuple(points[(j + 1) % 4]), (0, 255, 0), 2)

        # Display the decoded data on the frame
        cv2.putText(frame, data, (obj.rect.left, obj.rect.top),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

    # Display the frame with detected QR codes/barcodes
    cv2.imshow('QR Code and Barcode Reader', frame)

    # Exit the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

