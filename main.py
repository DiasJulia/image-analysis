import imageio
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

showImg()
plt.show()