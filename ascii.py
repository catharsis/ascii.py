#!/usr/bin/python
from PIL import Image
import os
import sys
symbols = "WEROI-"
def asciify(path):
    im = Image.open(path)
    width, height = im.size
    im = im.convert("P").resize((int(width / 7), int(height / 10)))
    width, height = im.size
    image_data = list(im.getdata())
    ch = 0
    matrix = {}
    while ch <= height:
        matrix[ch] = image_data[ch*width:(ch*width)+width]
        ch += 1

    for rown,data in matrix.items():
        for p in data:
            sys.stdout.write(symbols[p % len(symbols)])
        print()

if __name__ == '__main__':
    asciify(sys.argv[1])
