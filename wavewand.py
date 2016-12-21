# from PIL import Image
# import os
# from glob import glob
import sys
from wand.image import Image as wImage
from wand.display import display
import random

args = sys.argv
print args[1]

full_path = args[1] + '/*.jpg'
print full_path
# images = glob(full_path)
#
# times = int(args[2])
# print times
# for dex in range(0, times):
#     for file in images:
#         with Image(filename=file) as img:
#                 with img.clone() as i:
#                     imgCrop(i,(5,5,5,5),boxScale=1)
#                     i.crop(width=2550, height=2550, gravity='center')
#                     #random rotate 45, 90, 135
#                     r = random.choice([0,1,2,3])
#                     if (r > 0):
#                         i.rotate(45 * r)
#                         i.crop(width=1900, height=1900, gravity='center')
#                         display(i)
#                     else:
#                         i.resize(1900,1900)
#                     # i.save(filename='cover-alt-{0}.png'.format(r))
#                     # display(i)