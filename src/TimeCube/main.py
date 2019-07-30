from mpu6050 import mpu6050
import Adafruit_SSD1306
import Image
import ImageDraw
import ImageFont

display_padding = 10
font = ImageFont.load_default()

if __name__ == "__main__":
	#initalize IMU
	imu = mpu6050(0x68)

	#initialize screen
	display = Adafruit_SSD1306.SSD1306_128_32(24)
	display.begin()
	image = Image.new('1', (display.width, display.height))
	draw = ImageDraw.Draw(image)

	up_axis = ""
	prev_up_axis = ""
	while True:
		#read accelerometer
		accel_data = imu.get_accel_data()

		#determine up axis
		#print on screen
		accel_x_abs = abs(accel_data['x'])
		accel_x = accel_data['x']
		accel_y_abs = abs(accel_data['y'])
		accel_y = accel_data['y']
		accel_z_abs = abs(accel_data['z'])
		accel_z = accel_data['z']

		prev_up_axis = up_axis
		if accel_x_abs > accel_y_abs and accel_x_abs > accel_z_abs:
			if accel_x > 0:
				up_axis = "+X"
			else:
				up_axis = "-X"
		elif accel_y_abs > accel_x_abs and accel_y_abs > accel_z_abs:
			if accel_y > 0:
				up_axis = "+Y"
			else:
				up_axis = "-Y"
		elif accel_z_abs > accel_y_abs and accel_z_abs > accel_x_abs:
			if accel_z > 0:
				up_axis = "+Z"
			else:
				up_axis = "-Z"

		#display.clear()
		draw.text((display_padding, display_padding), prev_up_axis, font=font, fill=0)
		draw.text((display_padding, display_padding), up_axis, font=font, fill=255)
		display.image(image)
		display.display()
