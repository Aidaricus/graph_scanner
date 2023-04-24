import cv2

def show(image):
    w = image.shape[1] // 2
    h = image.shape[0] // 2

    resized = cv2.resize(image, (w, h))

    cv2.imshow('circle ', resized)
    cv2.waitKey()

