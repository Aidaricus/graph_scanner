import cv2

def make_tuple_for_graph(circles):
    res = []
    cnt = 1
    for circle in circles:
        res.append((circle, cnt))
        cnt += 1
    return res

def show(image):
    w = image.shape[1] // 2
    h = image.shape[0] // 2

    resized = cv2.resize(image, (w, h))

    cv2.imshow('circle ', resized)
    cv2.waitKey()

