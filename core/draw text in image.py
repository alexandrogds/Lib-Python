from PIL import Image, ImageDraw, ImageFont

# Load your image
image = Image.open('path_to_your_image.jpg')

# Initialize ImageDraw
draw = ImageDraw.Draw(image)

# Define font and size
font = ImageFont.truetype('path_to_your_font.ttf', 50)

# Define text and position
text = "Inspirational Text Here"
text_position = (50, 50)  # Adjust the position as needed

# Define text color (similar to image color with intermediate visibility)
text_color = (255, 255, 255, 128)  # RGBA

# Add text to image
draw.text(text_position, text, font=font, fill=text_color)

# Save the edited image
image.save('path_to_save_edited_image.jpg')

image.show()
