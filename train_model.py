import tensorflow as tf
import pandas as pd
import numpy as np

# Data inladen
df = pd.read_csv("training_data.csv")
X = df[["x", "y", "speed", "dx", "dy"]].values
y = df[["end_x", "end_y"]].values

# Model maken
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation="relu", input_shape=(5,)),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(2)
])

model.compile(optimizer="adam", loss="mse")

# Trainen
model.fit(X, y, epochs=100, verbose=1)

# Opslaan
model.save("roulette_predictor.h5")
