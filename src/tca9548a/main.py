import Adafruit_GPIO.I2C as I2C

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

padding=10
x=padding
top=padding
font = ImageFont.load_default()

class MUX_I2C:
    def __init__(self, port):
        self.port = port

    def get_i2c_device(self, address, busnum=None, i2c_interface=None, **kwargs):
        if busnum is None:
            busnum = I2C.get_default_bus()
        return MUX_Device(self.port, address, busnum, i2c_interface, **kwargs)

class MUX_Device(I2C.Device):
    def __init__(self, port, address, busnum, i2c_interface=None):
        self.port = port
        self._mux_i2c = I2C.get_i2c_device(0x70)

        super().__init__(address, busnum, i2c_interface)

    def __set_port(self):
        self._mux_i2c.writeRaw8(1 << self.port)

    def write8(self, register, value):
        self.__set_port()
        super().write8(register, value)

    def writeList(self, register, data):
        self.__set_port()
        super().writeList(register, data)

for i in range(4):
    # print(i)
    disp = Adafruit_SSD1306.SSD1306_128_64(rst=24, i2c=MUX_I2C(i))
    disp.begin()
    width = disp.width
    height = disp.height
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    draw.text((x,top), "Screen "+str(i), font=font, fill=255)
    disp.image(image)
    disp.display()

# disp0 = Adafruit_SSD1306.SSD1306_128_64(rst=24, i2c=MUX_I2C(0))
# disp1 = Adafruit_SSD1306.SSD1306_128_64(rst=24, i2c=MUX_I2C(1))
#
# disp0.begin()
# width0 = disp0.width
# height0 = disp0.height
# image0 = Image.new('1', (width0, height0))
# draw0 = ImageDraw.Draw(image0)
# draw0.text((x,top), "Screen 0", font=font, fill=255)
# disp0.image(image0)
# disp0.display()
#
# disp1.begin()
# width1 = disp1.width
# height1 = disp1.height
# image1 = Image.new('1', (width1, height1))
# draw1 = ImageDraw.Draw(image1)
# draw1.text((x,top), "Screen 1", font=font, fill=255)
# disp1.image(image1)
# disp1.display()
