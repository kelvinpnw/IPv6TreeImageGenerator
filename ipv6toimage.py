import argparse
parser = argparse.ArgumentParser(description='Generate image from IP list for IPv6 tree LED wall')
parser.add_argument('-l','--input_list',help='a list of IPv6 addresses (default stdin)')
parser.add_argument('-i','--input_image',help='existing image (default black)')
parser.add_argument('-o','--output_image',help='existing image (default reverse_out.png)', default='reverse_out.png')
args = parser.parse_args()

from PIL import Image
import fileinput
img = Image.open(args.input_image) if args.input_image else Image.new('RGB',(160,120))
skipped = False
for line in fileinput.input(args.input_list):
        line = line[15:-1]
        x,y = map(lambda x: int(x,10),line.split(':')[0:2])
        r,g,b = map(lambda x: int(x,16),line.split(':')[2:])
        print(x,y,r,g,b)
        if(x > 160 or y > 120 or r > 255 or g > 255 or b > 255):
                skipped = True
                continue
        img.putpixel((x,y),(r,g,b))
img.save(args.output_image)
if skipped:
        from warnings import warn
        warn('skipped some invalid pixels')
