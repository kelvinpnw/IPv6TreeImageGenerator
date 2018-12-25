import argparse
from warnings import warn
from PIL import Image

parser = argparse.ArgumentParser(description='Generate IP list for IPv6 tree LED wall')
parser.add_argument('input_file',help='an image')
parser.add_argument('-X','--XOffset',type=int,default=0,help='(default: 0)')
parser.add_argument('-Y','--YOffset',type=int,default=0,help='(default: 0)')
parser.add_argument('-f','--filter_transparent',action='store_true',help='ignore transparent pixels')
args = parser.parse_args()

img = Image.open(args.input_file)

if img.height + args.YOffset > 120:
    warn('Image too tall')
if img.width + args.XOffset > 160:
    warn('Image too wide')


for y in range(img.height):
    for x in range(img.width):
        r, g, b, a = img.getpixel((x, y))
        if(not args.filter_transparent or a == 255):
            r_hex='%02x' % r
            g_hex='%02x' % g
            b_hex='%02x' % b
            address = '2001:4c08:2028:'+str(x+args.XOffset)+':'+str(y+args.YOffset)+':'+r_hex+':'+g_hex+':'+b_hex;
            print(address)
