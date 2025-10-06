from adafruit_ssd1306 import SSD1306
import board
import busio
from PIL import Image, ImageDraw, ImageFont

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)

# OLED display setup
display = SSD1306(128, 64, i2c, addr=0x3C)

display.fill(0)
display.show()

# Create blank image for drawing.
image = Image.new("1", (display.width, display.height))
draw = ImageDraw.Draw(image)
draw.text((10, 25), "Hello Pi!", fill=255)

display.image(image)
display.show()
