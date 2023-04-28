import unittest

from models import circle, point, line

class TestCircle(unittest.TestCase):
    def setUp(self):
        self.tester_circle1 = circle(point(0, 0), 5)
        self.tester_circle2 = circle(point(1, 4), 20)
        self.tester_circle3 = circle(point(-2, -5), 4)
        self.tester_circle4 = circle(point(-2, 10), 10)
        self.tester_line1 = line(point(5, -5), point(-10, 16))

    def test_line_intersection(self):
        self.assertEqual(self.tester_circle1.line_intersection(self.tester_line1), True)
        self.assertEqual(self.tester_circle2.line_intersection(self.tester_line1), False)
        self.assertEqual(self.tester_circle3.line_intersection(self.tester_line1), False)
        self.assertEqual(self.tester_circle4.line_intersection(self.tester_line1), True)

if __name__ == "__main__":
    unittest.main()