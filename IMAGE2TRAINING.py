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
    baseHeight = 256
    png = Image.open(os.path.join(src,each))
    hpercent = (baseHeight / float(png.size[1]))
    wsize = int((float(png.size[0]) * float(hpercent)))
    png = png.resize((wsize, baseHeight), Image.Resampling.LANCZOS)
    ## Crop from center
    width, height = png.size
    left = (width - baseHeight)/2
    top = (height - baseHeight)/2
    right = (width + baseHeight)/2
    bottom = (height + baseHeight)/2
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
