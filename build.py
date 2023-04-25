import cv2
import numpy as np
import networkx as nx

import detector
import metods


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

def circles_of_line(line, nodes):
    res = []
    for circle in nodes:
        if (circle.line_intersection(line)):
            res.append(circle)
    return res

def build_graph(img):
    circles = detector.find_circles(img)
    lines = detector.find_lines(img)
    # Определим каждой вершины все прямые пересекающие эту окружности этих вершин
    normalize_circles(circles, lines)

    G = nx.Graph()

    nodes = metods.make_tuple_for_graph(circles)
    G.add_nodes_from(nodes)
    # Считаем всё круги и попробуем добавить в нашу структуру новый элемент

    if nodes is not None:

        for node in nodes:
            if node.lines is not None:

                for l in node.lines:
                    nodes_of_cur_line = circles_of_line(l, nodes)
                    for c in nodes_of_cur_line:
                        if (G.number_of_edges() >= G.number_of_nodes() * (G.number_of_nodes() - 1) / 2):
                            break
                        if (c != node):
                            # print(node, c)
                            G.add_edge(node, c)
            else:
                print ('LINES NOT FOUND')
    else: print("CIRCLES NOT FOUND")
    return G

def write_graph(graph, img, file, names):
    # cnt = 1
    print(names)
    for node in graph.nodes:
        cv2.circle(img, (node.center.x, node.center.y), node.radius, (128, 57, 24), 10)
        cv2.putText(img, names[node].text(), (node.center.x, node.center.y), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 255), 4)

    for circle1, circle2 in graph.edges:
        cv2.line(img, (circle1.center.x, circle1.center.y), (circle2.center.x, circle2.center.y), (0, 255, 0), 10)
    cv2.imwrite(file, img)
