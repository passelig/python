import cv2
import sys

s = 0  # Default to webcam
if len(sys.argv) > 1:
    s = sys.argv[1]

source = cv2.VideoCapture(s)

win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

frame_count = 0  # Counter
print('Press escape key to exit camera')
while cv2.waitKey(1) != 27:  # Escape key to exit
    has_frame, frame = source.read()
    if not has_frame:
        break

    # Get frame dimensions
    height, width, _ = frame.shape
    center_x, center_y = width // 2, height // 2

    # Draw a circle in the middle of the frame
    radius = min(height, width) // 10
    color = (0, 255, 0)  # Green
    thickness = 2

    cv2.circle(frame, (center_x, center_y), radius, color, thickness)
    cv2.imshow(win_name, frame)

    # Print frame count at the same spot in the command line
    frame_count += 1
    sys.stdout.write(f"\rFrame Count: {frame_count}")
    sys.stdout.flush()  # Ensures it updates properly

source.release()
cv2.destroyAllWindows()
