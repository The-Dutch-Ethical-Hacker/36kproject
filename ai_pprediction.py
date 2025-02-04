import tensorflow as tf
import numpy as np

# Laad getraind model
model = tf.keras.models.load_model("roulette_predictor.h5")

# Voorspel landingspositie
new_input = np.array([[500, 300, 20, 1, -1]])  # x, y, speed, dx, dy
prediction = model.predict(new_input)

print("AI Voorspelling:", prediction)
