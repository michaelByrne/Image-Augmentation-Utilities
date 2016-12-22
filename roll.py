#function implementing horizontal roll for magickwand/wand


def roll(im, delta):
    "Roll an image sideways"

    xsize = im.width
    ysize = im.height

    delta = delta % xsize
    if delta == 0: return im
    print delta, xsize, ysize
    # 0, 0, 200, 3300
    part1 = im.clone()
    part2 = im.clone()
    part1.crop(0, 0, width = delta, height = ysize)
    part2.crop(delta, 0, width = xsize, height = ysize)
    im.composite(part2, 0, 0)
    im.composite(part1, xsize-delta, 0)
    return im