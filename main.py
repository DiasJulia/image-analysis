import imageio
import numpy as np
import random
import matplotlib.pyplot as plt

pic = imageio.imread('paju.jpeg')

plt.figure(figsize = (5,5))

def redLayer():
    plt.imshow(pic[ : , : , 0])

def greenLayer():
    plt.imshow(pic[ : , : , 1])

def blueLayer():
    plt.imshow(pic[ : , : , 2])

def showImg():
    plt.imshow(pic)

def redFilter(num):
    val = (num *255)/100
    pic[:, :, 0] = val

def greenFilter(num):
    val = (num *255)/100
    pic[:, :, 1] = val

def blueFilter(num):
    val = (num *255)/100
    pic[:, :, 2] = val

def gradient(color):
    picture = []
    for x in range(0, 250):
        arrayx = []
        for y in range(0, 250):
            arrayy = []
            for z in range(0, 3):
                if(z == color):
                    val = (x * y * 3) / (5 * 10 ** 4 * 3)
                else:
                    val = 0
                arrayy.append(val)
            arrayx.append(arrayy)
        picture.append(arrayx)
    return np.array(picture)