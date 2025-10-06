import time
import board
import busio
import adafruit_mpu6050

# Initialisation of I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# Initialisation of MPU6050
mpu = adafruit_mpu6050.MPU6050(i2c)

print("Test MPU6050 : Appuyez sur Ctrl+C pour quitter")

try:
    while True:
        # Acceleration (x, y, z)
        accel = mpu.acceleration
        # Angular velocity (x, y, z)
        gyro = mpu.gyro
        # Temperature (°C)
        temp = mpu.temperature

        print(f"Acceleration : X={accel[0]:.2f} Y={accel[1]:.2f} Z={accel[2]:.2f} g")
        print(f"Gyroscope    : X={gyro[0]:.2f} Y={gyro[1]:.2f} Z={gyro[2]:.2f} °/s")
        print(f"Temperature  : {temp:.2f} °C")
        print("-" * 40)
        time.sleep(1)

except KeyboardInterrupt:
    print("Arrêt du test MPU6050")