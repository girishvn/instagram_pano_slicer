% File: instagram_pano_slicer.m
% Brief: script to slice panoramic img into multiple square imgs for insta
% Usage: change the panoImg value to the path of the pano image 
% The output images will be saved in same dir at the script

% Author: Girish Narayanswamy
% Date: 12 October 2018

panoImg = 'input_pano.jpg'; % change image path to pano image
img = imread(panoImg); % read in image
[height,width,dim] = size(img); % get height, width, and dimensions (RGB)

% Return if not horizontal panoramic image (image not applicable to insta)
if (height > width)
    disp('taller than wide');
    return;
end

numImgs = fix(width / height); % calc number of square imgs in pano
newWidth = numImgs * height; % calc width of cropped pano
start = fix((width - newWidth) / 2); % grabs pano from center of the img

% for loop to frame, crop, and save individual square images
for i = 1:numImgs
    startPix = start + (i - 1)*(height + 1);
    endPix = start + (i)*(height) + (i - 1);
    sqrImg = img(:,startPix:endPix,:);
    imwrite(sqrImg, ['output_img_',num2str(i),'.jpg']); 
end

disp('Images Built')

