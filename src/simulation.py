import time

def simulate_movement(path):
    for step in path:
        print(f"Robot moving to {step}")
        time.sleep(0.2)