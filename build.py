import cv2
import numpy as np

import detector
import metods
import networkx as nx

def normalize_circles(circles, lines):
    # Увеличим длину каждого круга до максимального
    max_circle = max(circles)
    for circle in circles:
        d = max_circle.radius - circle.radius
        circle.radius += d

    for circle in circles:
        if (circle.lines is None):
            ls = lines_of_circle(circle, lines)
            circle.set_lines(ls)
def lines_of_circle(circle, lines):
    res = []
    for line in lines:
        if (circle.line_intersection(line)):
            res.append(line)
    return res

def circles_of_line(line, circles):
    res = []
    for circle in circles:
        if (circle.line_intersection(line)):
            res.append(circle)
    return res

def build_graph(img):
    circles = detector.find_circles(img)
    lines = detector.find_lines(img)
    # TODO: Сделать нормальную проверку невалидности принятого изображения
    G = nx.Graph()

    G.add_nodes_from(sorted(circles, key = lambda circle: circle.center.x))

    # Определим каждой окружности все прямые пересекающие эту окружность
    normalize_circles(circles, lines)

    # Считаем всё круги и попробуем добавить в нашу структуру новый элемент
    if circles is not None:
        for circle in circles:
            # circle - первая окружность
            if circle.lines is not None:
                for l in circle.lines:
                    curles_of_cur_line = circles_of_line(l, circles)
                    for c in curles_of_cur_line:
                        if (G.number_of_edges() >= G.number_of_nodes() * (G.number_of_nodes() - 1) / 2):
                            break
                        if (c != circle):
                            cnt = G.number_of_edges()
                            G.add_edge(circle, c)
                            newcnt = G.number_of_edges()

                            circle_img = img.copy()

                            x1, y1 = l.point1.x, l.point1.y
                            x2, y2 = l.point2.x, l.point2.y
                            cv2.line(circle_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                            cv2.circle(circle_img, (x1, y1), 3, (0, 100, 100), 3)
                            cv2.circle(circle_img, (x2, y2), 3, (0, 100, 100), 3)

                            cv2.circle(circle_img, (circle.center.x, circle.center.y), 3, (100, 100, 100), 3)
                            cv2.circle(circle_img, (circle.center.x, circle.center.y), circle.radius,
                                       (100, 100, 100), 10)
                            cv2.circle(circle_img, (c.center.x, c.center.y), 3, (100, 200, 0), 3)
                            cv2.circle(circle_img, (c.center.x, c.center.y), c.radius,
                                       (100, 200, 0), 10)

                            # metods.show(circle_img)
    else: print("circles not found")
    return G
def write_graph(graph, img, file):
    cnt = 1
    for node in graph.nodes:
        cv2.circle(img, (node.center.x, node.center.y), node.radius, (100, 100, 100), 5)

        cv2.putText(img, '{}'.format(cnt), (node.center.x, node.center.y), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 255), 4)
        cnt += 1
    for circle1, circle2 in graph.edges:
        cv2.line(img, (circle1.center.x, circle1.center.y), (circle2.center.x, circle2.center.y), (0, 255, 0), 5)
    # metods.show(img)
    cv2.imwrite(file, img)


def show_iterativly(circles, lines, img):
    dict_of_lines = {}
    G = nx.Graph()
    G.add_nodes_from(circles)

    dict_of_lines = {}

    for cur_circle in circles:
        circle_img = img.copy()
        dict_of_lines[(cur_circle.center.x, cur_circle.center.y)] = []
        cv2.circle(circle_img, (cur_circle.center.x, cur_circle.center.y), 3, (0, 100, 100), 3)
        cv2.circle(circle_img, (cur_circle.center.x, cur_circle.center.y), cur_circle.radius, (255, 0, 255), 10)

        l = lines_of_circle(cur_circle, lines)

        if l is not None:
            for line in l:
                c = circles_of_line(line, circles)
                if c is not None:
                    for circle in c:
                        if (circle.line_intersection(line)):
                            # Нарисовать отрезок
                            x1, y1 = line.point1.x, line.point1.y
                            x2, y2 = line.point2.x, line.point2.y
                            cv2.line(circle_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                            cv2.circle(circle_img, (x1, y1), 3, (0, 100, 100), 3)
                            cv2.circle(circle_img, (x2, y2), 3, (0, 100, 100), 3)

                            # Нарисовать круг
                            cv2.circle(circle_img, (circle.center.x, circle.center.y), 3, (0, 100, 100), 3)
                            cv2.circle(circle_img, (circle.center.x, circle.center.y), circle.radius, (0, 122, 255), 10)

        metods.show(circle_img)
