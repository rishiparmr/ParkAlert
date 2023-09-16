import cv2
import pytesseract

def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


def preprocess_image(image):
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grayscale, (5, 5), 0)
    return blur

img = cv2.imread('ticket.png')
img = preprocess_image(img)
#img = thresholding(img)
#img = remove_noise (img)
output = ocr_core(img)

with open('output.txt', 'w') as f:  # 'output.txt' is the name of the file you want to create
    f.write(output)