#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Simon Matern
"""

import numpy as np
import cv2
import utils


def binarizeImage(img, thresh):
    """
    Given a coloured image and a threshold binarizes the image.
    Values below thresh are set to 0. All other values are set to 255
    """
    h, w, _ = img.shape
    binarized_img = np.zeros((h, w))

    for y in range(h):
        for x in range(w):
            if (img[y, x] < thresh).all():
                binarized_img[y, x] = 255

    return binarized_img

def smoothImage(img):    
    """
    Given a coloured image apply a blur on the image, e.g. Gaussian blur
    """
    blurred_img = cv2.GaussianBlur(img, (99, 99), 0)
    return blurred_img

def doSomething(img):
    """
    Given a coloured image apply any image manipulation. Be creative!
    """
    h, w, _ = img.shape
    face = img[20:h-20, 40:w-40]
    img[20:h-20, 40:w-40] = face[::-1,::-1,:]
    return img

def processImage(img):
    """
    Given an coloured image applies the implemented smoothing and binarization.
    """
    img = smoothImage(img)
    img = binarizeImage(img, 125)
    return img


if __name__=="__main__":
    img = cv2.imread("test.png")
    utils.show(img)
    
    img1 = smoothImage(img)
    utils.show(img1)
    cv2.imwrite("result1.jpg", img1)
    
    img2 = binarizeImage(img, 125)
    utils.show(img2)
    cv2.imwrite("result2.jpg", img2)
   
    img3 = processImage(img)
    utils.show(img3)
    cv2.imwrite("result3.jpg", img3)
    
    img4 = doSomething(img)
    utils.show(img4)
    cv2.imwrite("result4.jpg", img4)
