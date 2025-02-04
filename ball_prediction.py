import cv2
import numpy as np

# Video capture openen (0 voor webcam, of videobestand pad)
cap = cv2.VideoCapture(0)

# Sla vorige positie op voor snelheid en richting
prev_center = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Converteer naar HSV-kleurmodel
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Definieer de witte kleur voor detectie
    lower_white = np.array([0, 0, 168], dtype=np.uint8)
    upper_white = np.array([172, 111, 255], dtype=np.uint8)

    # Maak een mask voor wit
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # Zoek contouren
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Grootste contour selecteren (meest waarschijnlijke bal)
        largest_contour = max(contours, key=cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(largest_contour)

        if radius > 5:
            center = (int(x), int(y))

            # Teken de bal
            cv2.circle(frame, center, int(radius), (0, 255, 0), 2)

            # Bereken snelheid en richting
            if prev_center is not None:
                speed = np.linalg.norm(np.array(center) - np.array(prev_center))
                direction = (center[0] - prev_center[0], center[1] - prev_center[1])

                # Toon snelheid en richting
                cv2.putText(frame, f"Speed: {speed:.2f}", (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                cv2.putText(frame, f"Direction: {direction}", (10, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

            prev_center = center

    # Toon de output
    cv2.imshow("Ball Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
