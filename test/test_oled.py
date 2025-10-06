mport board
import busio
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont

i2c = busio.I2C(board.SCL, board.SDA)
display = SSD1306_I2C(128, 64, i2c, addr=0x3C)

display.fill(0)
display.show()

image = Image.new("1", (display.width, display.height))
draw = ImageDraw.Draw(image)
draw.text((10, 25), "Hello Pi!", fill=255)
display.image(image)
display.show()