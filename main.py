import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('images/hirono (2).jpeg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


_, image_binary = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)


kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))


erosion = cv2.erode(image_binary, kernel, iterations=1)
dilation = cv2.dilate(image_binary, kernel, iterations=1)


opening = cv2.morphologyEx(image_binary, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(image_binary, cv2.MORPH_CLOSE, kernel)


gradient = cv2.morphologyEx(image_binary, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(image_binary, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(image_binary, cv2.MORPH_BLACKHAT, kernel)


titles = ['Citra Asli', 'Biner', 'Erosion', 'Dilation',
          'Opening', 'Closing', 'Gradient', 'Top Hat', 'Black Hat']
images = [image_gray, image_binary, erosion, dilation,
          opening, closing, gradient, tophat, blackhat]

plt.figure(figsize=(15, 10))
for i in range(len(images)):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
