# Update all images within ~/supplier-data/images directory to the following specifications:
# Size: Change image resolution from 3000x2000 to 600x400 pixel
# Format: Change image format from .TIFF to .JPEG

#!/usr/bin/env python3
import os
from PIL import Image

directory = 'supplier-data/images/'

# iterate over files in
# that directory
for filename in os.listdir(directory):
  f = os.path.join(directory, filename)
  # checking if it is a file
  if os.path.isfile(f) and not filename.startswith('.') and filename.endswith('.tiff'):
    outfile = directory + filename
    outfile = outfile.replace(".tiff", ".jpeg")
    with Image.open(f) as im:
      im.convert('RGB').resize((600,400)).save(outfile)