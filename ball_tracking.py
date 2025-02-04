import cv2
import numpy as np

def detect_ball(frame):
    # Converteer het beeld naar HSV (beter voor kleurdetectie)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Definieer kleurwaarden voor witte bal (kan aangepast worden)
    lower_white = np.array([0, 0, 180])  # Lagere grens wit
    upper_white = np.array([255, 60, 255])  # Hogere grens wit
    
    # Maak een masker om alleen de witte bal te zien
    mask = cv2.inRange(hsv, lower_white, upper_white)
    
    # Vind contouren van de bal
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 50:  # Negeer kleine ruis
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)
            
            # Teken een cirkel om de bal
            cv2.circle(frame, center, radius, (0, 255, 0), 2)
            return center  # Coördinaten van de bal
    return None

def main():
    cap = cv2.VideoCapture(0)  # Open de camera
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        ball_position = detect_ball(frame)
        if ball_position:
            print(f"Bal positie: {ball_position}")
        
        cv2.imshow('Roulette Ball Tracking', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
