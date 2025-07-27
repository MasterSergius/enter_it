"""
Draw triangles (NxN)

Example, 3x3:

*     ***    *  ***
**    **    **   **
***   *    ***    *
"""


# Might be used for other Shapes: Square(Shape), Circle(Shape), etc.
class Shape:
    def __init__(self, size: int):
        self.size = size

    def draw(self):
        raise NotImplementedError


class Triangle(Shape):
    def draw(self):
        raise NotImplementedError


class Triangle1(Triangle):
    def draw(self):
        for i in range(self.size):
            print("*" * (i + 1))


class Triangle2(Triangle):
    def draw(self):
        for i in range(self.size):
            print("*" * (self.size - i))


class Triangle3(Triangle):
    def draw(self):
        for i in range(self.size):
            print(" " * (self.size - i - 1) + "*" * (i + 1))


class Triangle4(Triangle):
    def draw(self):
        for i in range(self.size):
            print("*" * (self.size - i) + " " * (i + 1))


def main():
    for triangle in (Triangle1(5), Triangle2(5), Triangle3(5), Triangle4(5)):
        triangle.draw()
        print()


main()
