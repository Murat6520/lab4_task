import unittest


def is_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
        return True
    else:
        return False


class TriangleTestCase(unittest.TestCase):

    def test_valid_triangle(self):
        side1 = 3
        side2 = 4
        side3 = 5
        self.assertTrue(is_triangle(side1, side2, side3))

    def test_equilateral_triangle(self):
        side1 = 2
        side2 = 2
        side3 = 2
        self.assertTrue(is_triangle(side1, side2, side3))

    def test_invalid_triangle(self):
        side1 = 5
        side2 = 6
        side3 = 12
        self.assertFalse(is_triangle(side1, side2, side3))

    def test_zero_sides(self):
        side1 = 0
        side2 = 0
        side3 = 0
        self.assertFalse(is_triangle(side1, side2, side3))

    def test_triangle_inequality(self):
        side1 = 7
        side2 = 1
        side3 = 2
        self.assertFalse(is_triangle(side1, side2, side3))


if __name__ == '__main__':
    unittest.main()
