import board
import busio
from adafruit_ssd1306 import SSD1306
from PIL import Image, ImageDraw, ImageFont

# Init I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# Init display
display = SSD1306(width=128, height=64, i2c=i2c, addr=0x3C)

# Clear display
display.fill(0)
display.show()

# Create image for drawing
image = Image.new("1", (display.width, display.height))
draw = ImageDraw.Draw(image)

# Write text
draw.text((10, 25), "Hello Pi!", fill=255)

# Display image on screen
display.image(image)
display.show()

