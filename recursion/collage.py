#!/usr/bin/env python3
import argparse
import os
from PIL import Image               # pip3 install pillow
from foldersearch import find_images


THUMNAILS_PER_ROW = 4
THUMBNAIL_WIDTH = 200
THUMBNAIL_HEIGHT = 200



########################
###  Main program

def main(args):
    '''
    Creates a collage by recursively finding images in a directory path.
    '''
    # find the images
    imgpaths = []
    for filepath in find_images(os.path.abspath(args.searchpath)):
        imgpaths.append(filepath)
    if len(imgpaths) == 0:
        print('No images found')
        return

    # create a new, RGB image

    # place the thumbnails
    for imgnum, imgpath in enumerate(imgpaths):
        print(f'=> {imgpath}')
        # open the image and convert to RGB
        # resize to a thumnail
        # paste in next position

    # save the image
    print(f'Writing {args.collage}')


########################
###  Bootstrap

parser = argparse.ArgumentParser(description='Creates a collage by recursively finding images in a directory path')
parser.add_argument('collage', help='file name to write the collage to')
parser.add_argument('searchpath', help='directory path to start searching')
args = parser.parse_args()
main(args)
