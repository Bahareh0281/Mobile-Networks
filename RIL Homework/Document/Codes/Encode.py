# importing openCV for image processing and numpy for numerical operations
import cv2
import numpy as np

# reading input image
image = cv2.imread('pic1.jpg')
plain_text = "name to ramz mishavad#"
binary_plain_text = list()
counter = 0

for i in range(len(plain_text) - 1, -1, -1):
    # converts into its Unicode code point
    temp = ord(plain_text[i])
    #convert the unicode to binary and store it in reversed oreder
    for _ in range(8):
        binary_plain_text.append(temp % 2)
        temp //= 2
binary_plain_text = list(reversed(binary_plain_text))

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if(counter == len(binary_plain_text)):
            break
        for k in range(image.shape[2]):
            # calculate the difference between the LSB of the pixel value and the next bit of the binary plaintext message.
            # then xor it with the original pixel value
            image[i, j, k] ^= abs(binary_plain_text[counter] - (image[i, j, k] & 1))
        counter += 1

cv2.imwrite('Encoded.png', image)