import sys
from PIL import Image

img = Image.open(sys.argv[1])
img = img.convert('RGB')

for y in range(img.height):
    for x in range(img.width):
        r, g, b = img.getpixel((x, y))
        r_hex='%02x' % r
        g_hex='%02x' % g
        b_hex='%02x' % b
        address = '2001:4c08:2028:'+str(x+sys.argv[2])+':'+str(y+sys.argv[3])+':'+r_hex+':'+g_hex+':'+b_hex;
        print(address)
