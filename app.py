from flask import Flask, request, jsonify
from io import BytesIO
import base64
import cv2
import numpy as np
from object_detection import detect_objects
from movement_analysis import analyze_movement
from prediction_logging import log_prediction

app = Flask(__name__)

@app.route('/start-prediction', methods=['POST'])
def start_prediction():
    data = request.get_json()
    image_data = data['image']  # Base64 afbeelding uit JavaScript

    # Verwijder de prefix "data:image/jpeg;base64,"
    image_data = image_data.split(",")[1]

    # Zet de Base64-string om naar een bytearray
    img_bytes = base64.b64decode(image_data)
    img_array = np.frombuffer(img_bytes, dtype=np.uint8)

    # Decodeer de afbeelding
    frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    # Voer objectdetectie en bewegingsanalyse uit
    detected_objects = detect_objects(frame)
    predicted_position = analyze_movement(detected_objects)

    # Log de voorspelling
    log_prediction(predicted_position, actual_position)

    # Stuur de voorspelling terug naar de frontend
    return jsonify({'prediction': predicted_position})

if __name__ == '__main__':
    app.run(debug=True)
