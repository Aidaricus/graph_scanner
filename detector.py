import cv2
import numpy as np
from filters import red_filter
from models import circle, point, line
# detect_cicrles
def find_circles(img):
    # my_photo = cv2.imread('images/graph4.jpg')
    filterd_image = cv2.medianBlur(img, 7)
    rows = img.shape[0]

    #red filter
    red_filtered = red_filter(filterd_image)

    # gray
    img_gray = cv2.cvtColor(red_filtered, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 1, rows / 10,
                               param1=90, param2=30,
                               minRadius=1, maxRadius=200)
    circles_list = []
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:

            center = point(i[0], i[1])
            radius = i[2]
            circles_list.append(circle(center, radius))
    return circles_list

def find_lines(img):
    filterd_image = cv2.medianBlur(img, 7)
    img_gray = cv2.cvtColor(filterd_image, cv2.COLOR_BGR2GRAY)
    rows = img_gray.shape[0]
    edges = cv2.Canny(img_gray, 50, 150, apertureSize=3)

    # red filter
    red_filtered = red_filter(filterd_image)

    img_gray = cv2.cvtColor(red_filtered, cv2.COLOR_BGR2GRAY)

    lines_list = []
    lines = cv2.HoughLinesP(
        img_gray,  # Input edge image
        1,  # Distance resolution in pixels
        np.pi / 180,  # Angle resolution in radians
        threshold=300,  # Min number of votes for valid line
        minLineLength=50,  # Min allowed length of line
        maxLineGap= 200  # Max allowed gap between line for joining them
    )


    # Iterate over points
    if lines is not None:
        for points in lines:
            x1, y1, x2, y2 = points[0]
            lines_list.append(line(point(x1, y1), point(x2, y2)))

    else: print("LINES NOT FOUND")

    return lines_list