import unittest

import cv2

from detector import find_circles
class TestFindCirlces(unittest.TestCase):
    def setUp(self):
        self.tester_1 = find_circles(cv2.imread('test_images/test_graph_image_1.png'))
        self.tester_2 = find_circles(cv2.imread('test_images/test_graph_image_2.png'))
        self.tester_3 = find_circles(cv2.imread('test_images/test_graph_image_3.png'))
        self.tester_4 = find_circles(cv2.imread('test_images/test_graph_image_4.png'))

    def test_count_of_lines(self):
        self.assertEqual(len(self.tester_1), 3)
        self.assertEqual(len(self.tester_2), 6)
        self.assertEqual(len(self.tester_3), 3)
        self.assertEqual(len(self.tester_4), 5)

if __name__ == "__main__":
    unittest.main()