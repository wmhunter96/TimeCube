import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

import Image
import ImageDraw
import ImageFont

RST = 24

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height

image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width-1,height-1), outline=255, fill=0)

padding=2
x=padding
top=padding
bottom=height-1-padding
font = ImageFont.load_default()
draw.text((x,top), "Hello, World!", font=font, fill=255)


disp.image(image)
disp.display()
