# background_remove.py
# pip install rembg
# pip install pillow
# pip install onnxruntime
from rembg import remove
from PIL import Image

input_dir = 'background_remove_sample.png'
output_dir = 'background_removed.png'

img = Image.open(input_dir)

pro = remove(img)

pro.save(output_dir)
