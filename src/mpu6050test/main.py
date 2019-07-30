from mpu6050 import mpu6050

sensor = mpu6050(0x68)

accel_data = sensor.get_accel_data()
gyro_data = sensor.get_gyro_data()

print("accel: " + str(accel_data))
print("gyro: " + str(gyro_data))
