# barcode_generator.py
# pip install python-barcode pillow
from barcode import get, writer
from PIL import Image as img

user_input = input("Enter data to encode in barcode: ")

code = get('code128', user_input, writer=writer.ImageWriter())

file_name = code.save('barcode')

image_display = img.open(file_name)
image_display.show()
