from PIL import Image
from tqdm import tqdm
import os

src = "./images"
dst = "./data/"

try:
    os.mkdir(dst)
    print("Made {}".format(dst))
except:
    pass


for each in tqdm(os.listdir(src)):
    ## Resize image to have a height of baseHeight
    base = 256
    png = Image.open(os.path.join(src,each))
    width, height = png.size

    ## Basing scale off smallest side stops black bars from appearing on the images
    if height <= width:
        ##Resize if height is smallest side
        hpercent = (base / float(png.size[1]))
        wsize = int((float(png.size[0]) * float(hpercent)))
        png = png.resize((wsize, base), Image.Resampling.LANCZOS)
    elif width < height:
        ##Resize if width is smallest side
        wpercent = (base / float(png.size[0]))
        hsize = int((float(png.size[1]) * float(wpercent)))
        png = png.resize((base, hsize), Image.Resampling.LANCZOS)

    ## Crop from center
    width, height = png.size
    left = (width - base)/2
    top = (height - base)/2
    right = (width + base)/2
    bottom = (height + base)/2

    png = png.crop((left, top, right, bottom))
    # print each
    if png.mode == 'RGBA':
        png.load() # required for png.split()
        background = Image.new("RGB", png.size, (0,0,0))
        background.paste(png, mask=png.split()[3]) # 3 is the alpha channel
        background.save(os.path.join(dst,each.split('.')[0] + '.jpg'), 'JPEG')
    else:
        png = png.convert('RGB')
        png.convert('RGB').save(os.path.join(dst,each.split('.')[0] + '.jpg'), 'JPEG')
