import os
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageChops, ImageStat

def psnr(img1, img2):
    diff_img = ImageChops.difference(img1, img2)
    stat = ImageStat.Stat(diff_img)
    mse = sum(stat.sum2) / len(stat.count) / stat.count[0]
    return 10 * math.log10(255 ** 2 / mse)

filename = sys.argv[1]
img = Image.open(filename + '.JPG', 'r').convert('L')

if not os.path.isdir(filename):
    os.mkdir(filename)

rates = []
psnrs = []

for q in range(1, 10):
    quality = 10 * q
    savename = filename + '/' + str(quality) + '.JPG'
    img.save(savename, quality=quality)

    comp = Image.open(savename, 'r')
    comp_bits = os.path.getsize(savename) * 8
    comp_size = img.size[0] * img.size[1]
    rates.append(comp_bits / comp_size)
    psnrs.append(psnr(img, comp))

print(rates)
plt.plot(rates, psnrs)
plt.show()
