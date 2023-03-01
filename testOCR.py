# import easyocr
# import cv2
# im_gray = cv2.imread('testEasyOCR.png', cv2.IMREAD_GRAYSCALE)
# (thresh, im_bw) = cv2.threshold(im_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# reader = easyocr.Reader(['en', 'en'])
# result = reader.readtext(im_bw)
# cv2.imwrite('hasil.png',im_bw)
# print(result)

import cv2

# read the image in colored format
# img = cv2.imread('testEasyOCR.png')

# # convert to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # apply binary thresholding
# thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]



# # save the binary image
# cv2.imwrite('output2.png', thresh)
from PIL import Image
from PIL import ImageEnhance

def deskew(image):
    """Deskew an image using its contours."""
    # Find contours in the image
    contours = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]

    # Find the largest contour
    largest_contour = max(contours, key=cv2.contourArea)

    # Find the orientation of the largest contour
    _, _, angle = cv2.minAreaRect(largest_contour)

    # Rotate the image to correct the skew
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated


# Open image
#img = Image.open("testEasyocr.png")
img = cv2.imread('testEasyocr.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a binary threshold to obtain a binary image
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
img = deskew(binary)
cv2.imwrite('Result.png', img)
#cv2.imsave('Result', img)
# # Enhance contrast
# enhancer = ImageEnhance.Contrast(img)
# img = enhancer.enhance(5)  # Increase contrast by 50%

# # Save output image
# img.save("output_image.png")

