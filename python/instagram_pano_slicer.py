# File: instagram_pano_slicer.m
# Brief: script to slice panoramic img into multiple square imgs for insta
# Usage: change the panoImg value to the path of the pano image
# The output images will be saved in same dir at the script
# To use image formats other than jpg please download load PIL or Pillow in addition to the imported packages

# Author: Girish Narayanswamy
# Date: 12 October 2018

import matplotlib.pyplot as plt  # needed for image reads and saves
import sys  # for error reporting and termination
import numpy as np  # to convert read in img data as a numpy array

img = plt.imread('images/inputImg.jpg')  # change image path to pano image
(height, width, dim) = img.shape  # read in image
imgData = np.array(img)  # get height, width, and dimensions (RGB)

# Return if not horizontal panoramic image (image not applicable to insta)
if height > width:
    print('height is greater than width')
    sys.exit(-1)

numImgs = int(width / height)  # calc number of square imgs in pano
newWidth = numImgs * height  # calc width of cropped pano
start = int((width - newWidth) / 2)  # grabs pano from center of the img

# for loop to frame, crop, and save individual square images
for i in range(numImgs):
    startPix = start + i*(height + 1)
    endPix = start + (i + 1)*height + i

    sqrImg = imgData[:, startPix:endPix, :]
    img = plt.imsave('images/output_img_' + str(i + 1) + '.jpg', sqrImg, format='jpg')

print('Images Built')