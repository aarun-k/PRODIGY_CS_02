# Pixel-Manipulation-for-Image-Encryption

**Image Encryption Tool**

A Simple Image Encryption Tool using Pixel Manipulation with Python

**Overview**

This Python script provides a simple yet effective image encryption tool that allows users to encrypt and decrypt images using basic mathematical operations such as addition, subtraction, division, or swapping of pixels with a given key.

**Requirements**
+ Python 3.x
+ Pillow (PIL fork)

**Installation**

Install the required packages using pip:
`pip install pillow`

**Encryption Methods**
+ Addition (add): Adds the encryption key to each pixel value.
+ Subtraction (sub): Subtracts the encryption key from each pixel value.
+ Division (div): Divides each pixel value by (key + 1) and takes the remainder.
+ Swap (swap): Reverses the image vertically (simple pixel swapping).
