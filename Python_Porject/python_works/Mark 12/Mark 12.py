import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import time

for n in range(1,7):
    st = '%d'%n
    pic = 'image'+st+'.png'
    img = mpimg.imread(pic)
    plt.imshow(img)
    plt.show()
    plt.close()