from PIL import Image
import time
import sys

print str(sys.argv[1])

IMAGE = Image.open(sys.argv[1])
PIXEL_COUNT = IMAGE.size[0] * IMAGE.size[1]

IMG_DATA = IMAGE.load()
RANGE_Y = xrange(IMAGE.size[0])
RANGE_X = xrange(IMAGE.size[1])
IMG_DATA = [[IMG_DATA[y, x] for y in RANGE_Y] for x in RANGE_X]

def colorAverage ():
    r, g, b = 0, 0, 0
    for x in RANGE_X:
        for y in RANGE_Y:
            temp = IMG_DATA[x][y]
            r += temp[0]
            g += temp[1]
            b += temp[2]
    return r/PIXEL_COUNT, g/PIXEL_COUNT, b/PIXEL_COUNT

def colorDominant ():
    r, g, b = 0, 0, 0
    for x in RANGE_X:
        for y in RANGE_Y:
            temp = IMG_DATA[x][y]
            r += temp[0]
            g += temp[1]
            b += temp[2]
    if r > g and r > b :
        return "RED"

    if g > r and g > b :
        return "GREEN"        

    if b > r and b > g :
        return "BLUE"   

start = time.time()
COLOR_AVG = colorAverage()
end = time.time()
duration = end - start

print round(duration, 4), "seconds"
print "average color: rgb(%s, %s, %s)" % (COLOR_AVG)
print "dominant color: %s" % colorDominant()
