import csv

# Voorbeeldgegevens opslaan
data = [
    [500, 300, 20, 1, -1, 700, 100],  # x, y, snelheid, dx, dy, eind_x, eind_y
    [200, 400, 15, -1, -1, 100, 50]
]

# Opslaan als CSV
with open('training_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["x", "y", "speed", "dx", "dy", "end_x", "end_y"])
    writer.writerows(data)
