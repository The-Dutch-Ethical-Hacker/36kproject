def analyze_movement(ball_position, wheel_positions, speed, bounce_factor):
    # Eenvoudige logica voor beweginganalyse
    predicted_position = ball_position + (speed * bounce_factor)
    
    return predicted_position
