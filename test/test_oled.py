import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# Init I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# Init display
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

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
