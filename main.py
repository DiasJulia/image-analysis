import imageio
import matplotlib.pyplot as plt

pic = imageio.imread('paju.jpeg')

plt.figure(figsize = (5,5))

plt.imshow(pic)

plt.title('R channel')
plt.imshow(pic[ : , : , 2])
print(pic[2])

print('Value of only R channel {}'.format(pic[ 1, 1, 0]))
print('Value of only G channel {}'.format(pic[ 1, 1, 1]))
print('Value of only B channel {}'.format(pic[ 1, 1, 2]))
plt.show()