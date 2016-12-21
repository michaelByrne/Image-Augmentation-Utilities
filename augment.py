from PIL import Image
import os
from glob import glob
import sys

def roll(image, delta):
    "Roll an image sideways"

    xsize, ysize = image.size

    delta = delta % xsize
    if delta == 0: return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    part1.load()
    part2.load()
    image.paste(part2, (0, 0, xsize-delta, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))

    return image

args = sys.argv
print args[1]

full_path = args[1] + '/*.jpg'
print full_path
images = glob(full_path)

dex = 0
for img in images:
	print img
	if os.stat(img).st_size == 0:
		print "got empty file at " + str(img)
	try:
		im=Image.open(img)
	except IOError:
		print "bad file at " + str(IOError)
		print "deleting " + str(img)
		os.remove(img)
	else:
		#random params: roll (300, 1000), transform(45, 315), 
		new_img = im.copy()
		box = (0, 600, 2400, 2900)
		new_img = new_img.crop(box)
		new_img.save("images/" + str(dex) + "_copy_normal.jpg")
		dex += 1
