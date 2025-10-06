import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

servo_channel = 0

print("Test servo : Movement from 0° to 180° and back. Press Ctrl-C to stop.")

try:
    while True:
        # Mouvement de 0° à 180°
        for angle in range(0, 181, 10):
            kit.servo[servo_channel].angle = angle
            time.sleep(0.5)
        # Mouvement de 180° à 0°
        for angle in range(180, -1, -10):
            kit.servo[servo_channel].angle = angle
            time.sleep(0.5)
except KeyboardInterrupt:
    print("Test stopped by user")