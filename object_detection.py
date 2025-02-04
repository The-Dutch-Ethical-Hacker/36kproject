import cv2
import tensorflow as tf
import numpy as np

# Laad je model
model = tf.keras.models.load_model('path_to_model.h5')

def detect_objects(frame):
    # Voorbeeld van objectdetectie (moet verder worden uitgewerkt)
    resized_frame = cv2.resize(frame, (224, 224))
    input_data = np.expand_dims(resized_frame, axis=0)
    predictions = model.predict(input_data)
    
    return predictions
