#!python

import os, sys, stat
from pdf2image import convert_from_path

from PIL import Image
import PIL.ImageOps, PIL.ImageChops

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)
#print str(sys.argv[1])

size1 = 306,991
size2 = 696, 1109
infile = str(sys.argv[1])
outfile = infile.split(".")
outfile = outfile[0]+'.jpg'

pages = convert_from_path(infile, 500)

for page in pages:
    w, h = page.size
    crop_area = 300, 100, w-200, h #DP -> Brother -> Brother DK-22205 Endlos-Etikett 62 mm
    page = page.crop(crop_area)
    page = page.resize(size1, PIL.Image.ANTIALIAS)
    page.save(outfile, 'JPEG')
print "Converted and resized successfully..."

# Set a file write by others.
os.chmod(outfile, stat.S_IRWXO)
print "Changed mode successfully..."
print "Done!"

# print out
printer = "file:///dev/usb/lp2"
mode = "linux_kernel"
model = "QL-800"
label1 = "29x90"
label2 = "62x100"

# requires: pip install brother_ql 
os.system("brother_ql -p "+printer+" -b "+mode+" -m "+model+" print -l "+label1+" "+outfile)

