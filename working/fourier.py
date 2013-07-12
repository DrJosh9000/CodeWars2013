#!/usr/bin/env python

import random
import string
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import misc
import itertools

#n = np.zeros((256,256))
#n = np.mgrid[0:256,0:256]
#n[60:80, 20:40] = np.exp(np.random.uniform(0, 2*np.pi, (20, 20)))

prism = misc.imread('/Users/josh/Code/CodeWars2013/refract.png')
#plt.imshow(prism)
#plt.show()

secret = misc.imread('/Users/josh/Code/CodeWars2013/secret.png')

encoded = (np.bitwise_and(prism,254)) + (secret % 2)

for i in range(16):
    for j in range(16):
        encoded[i*32:(i+1)*32,j*32:(j+1)*32] = np.rot90(encoded[i*32:(i+1)*32,j*32:(j+1)*32])

#plt.imshow(encoded)
#plt.show(1)

misc.imsave('/Users/josh/Code/CodeWars2013/encoded.png', encoded)
encoded = misc.imread('/Users/josh/Code/CodeWars2013/encoded.png')

for i in range(16):
    for j in range(16):
        encoded[i*32:(i+1)*32,j*32:(j+1)*32] = np.rot90(encoded[i*32:(i+1)*32,j*32:(j+1)*32],3)
        
decoded = (encoded % 2) * 255
plt.imshow(decoded)
plt.show()

#im = np.fft.fft2(n).real
#plt.imshow(im, cmap=plt.cm.gray)
#plt.show()