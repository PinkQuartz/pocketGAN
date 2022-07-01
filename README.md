# pocketGAN

## Overview
Based of the pokeGAN featured in [this](https://youtu.be/yz6dNf7X7SA) video on Youtube by Siraj Raval.

The original pokeGAN code comes from [this](https://github.com/moxiegushi/pokeGAN) project by @moxiegushi. All credit for actually understanding tensorflow goes to them, I just tidied it up a bit :)

## What is pocketGAN?
pocketGAN is a low level, simple GAN built using tensorflow. With a desire to try out the creative side of GANs, and a college student budget preventing me from getting a Nvidia graphics card, I decided to explore CPU options using tensorflow. Eventually I stumbled upon the aforementioned pokeGAN, but quite a few issues left much to be desired. First, the image processing was broken into two steps, the second of which wasn't even used in the end product despite being helpful. I decided to merge the two into one step. Second, the image processing made no attempt to scale the images to preserve detail, cropping it down to 256 no matter how much of the subject was lost. poketGAN now scales the height to 256 (and width proportionally), then crops to the center to preserve detail. Third, pokeGAN normalized images from 0 to 1, leaving the images quite washed out. This is now fixed by normalizing the images from -1 to 1. Most of these issues were pointed out by users in the issues tab of pokeGAN, but none were fixed. I also added some nice TQDM progress bars so you know what your computer is actually working on. Hopefully this GAN will be useful to someone, either as an entry to the field, a tool, or a starting point for an even better version :)

As poke is derived from the Japanese word for pocket, Poketto, and this GAN is pretty lightweight compared to other options out there, I decided pocketGAN was a fitting name.

## Dependencies
I highly recommend setting up a Conda environment for this project, as it makes everything nice and neat and conda install is required for older versions of tensorflow. All other packages can be installed via pip.

```
Pillow
tqdm
numpy
opencv_python
scipy
tensorflow=1.14
```

## Usage
1. Download/Make data set and put it in /images (make sure to delete the txt file in there, that jsut to allow it to be uploaded to GitHub)
2. *python IMAGE2TRAINING.py*
3. All training images will now be scaled properly and in the data file
4. *python pocketGAN.py*
5. Your computer is now training away! Every 5 epochs an 8x8 image of examples will be saved, and every 50 a checkpiont will be made (the program should automatically load in checkpoints to continue from, but that was one of the original issues I had to fix, so I can't 100% guarentee that taped up piece of code will work perfectly). Also give it time!! Since were not using CUDA and GPU here, the process will be much slower. 

## TODO
- [ ] Take care of some of the future warnings of numpy
- [ ] Better saving and loading of checkpoints
- [ ] Single image generation mode
- [ ] Option to change "newTest" and the like to custom names easily (for now just in tweaking code)
