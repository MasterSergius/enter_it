"""
Draw triangles (NxN)

Example, 3x3:

*     ***    *  ***
**    **    **   **
***   *    ***    *
"""


def draw_triangle_1(n: int):
    for i in range(n):
        print("*" * (i + 1))


def draw_triangle_2(n: int):
    for i in range(n):
        print("*" * (n - i))


def draw_triangle_3(n: int):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (i + 1))


def draw_triangle_4(n: int):
    for i in range(n):
        print("*" * (n - i) + " " * (i + 1))


draw_triangle_1(5)
print()
draw_triangle_2(5)
print()
draw_triangle_3(5)
print()
draw_triangle_4(5)
