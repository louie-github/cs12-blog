#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from arya import Point
from prac01d import is_in_triangle


def is_in_triangle_2(A: Point, B: Point, C: Point, P: Point):
    if (
        P[0] > min((A, B, C), key=lambda p: p[0])[0]
        or P[0] > max((A, B, C), key=lambda p: p[0])[0]
        or P[1] > min((A, B, C), key=lambda p: p[1])[1]
        or P[1] > max((A, B, C), key=lambda p: p[1])[1]
    ):  # out of bounds, strictly
        return True


MAX_INT = 10**15


def test_is_in_triangle():
    assert is_in_triangle((0, 0), (10, 30), (30, 10), (15, 15))
    assert not is_in_triangle((0, 0), (10, 30), (30, 10), (45, 45))

    # "Normal triangles"
    assert is_in_triangle((0, 0), (4, 0), (0, 4), (1, 1))
    assert not is_in_triangle((0, 0), (4, 0), (0, 4), (0, 5))
    assert not is_in_triangle((0, 0), (4, 0), (0, 4), (4, 2))
    # Same slope as one of the lines
    assert not is_in_triangle((0, 0), (4, 0), (0, 4), (-1, 5))
    # "Normal triangles" with negative and large coordinates
    assert is_in_triangle(
        (-(10**10), -(10**10)), (10**10, 10**10), (-(10**10), 10**5), (1, 1)
    )
    assert not is_in_triangle(
        (-(10**10), -(10**10)),
        (10**10, 10**10),
        (-(10**10), 10**5),
        (-(10**15), 10**15),
    )
    # Normal triangles with points on the boundary
    assert is_in_triangle((-3, 0), (0, 4), (3, 0), (0, 0))
    assert is_in_triangle((-3, 0), (0, 3), (3, 0), (-2, 1))
    assert is_in_triangle((-3, 0), (0, 3), (3, 0), (0, 3))
    # Degenerate triangles, points outside boundary
    assert not is_in_triangle((-3, 0), (3, 0), (3, 0), (1, 1))
    assert not is_in_triangle((0, 0), (0, 0), (0, 0), (1, 1))
    assert not is_in_triangle((0, 0), (0, 0), (3, 5), (3, 3))
    assert not is_in_triangle((0, 0), (0, 0), (0, 5), (0, 6))
    # Degenerate triangles, points inside boundary
    assert is_in_triangle((-3, 0), (3, 0), (3, 0), (0, 0))
    assert is_in_triangle((0, 0), (0, 0), (0, 0), (0, 0))
    assert is_in_triangle((0, 0), (0, 0), (3, 3), (1, 1))
    assert is_in_triangle((0, 0), (0, 0), (3, 3), (3, 3))
    # Degenerate triangles, three points on a line
    assert is_in_triangle((0, 0), (0, 2), (0, 3), (0, 1))
    assert is_in_triangle((0, 0), (0, 2), (0, 3), (0, 2))
    assert not is_in_triangle((0, 0), (0, 2), (0, 4), (1, 0))
    assert not is_in_triangle((0, 0), (0, 2), (0, 4), (1, 2))
    assert not is_in_triangle((0, 0), (0, 2), (0, 4), (0, 5))
    # Tiny triangles
    assert not is_in_triangle((-3, 0), (3, 1), (3, 0), (1, 1))
    # Huge triangles
    assert is_in_triangle(
        (-MAX_INT, -MAX_INT), (MAX_INT, 0), (-MAX_INT, MAX_INT), (0, 0)
    )
    assert not is_in_triangle(
        (-MAX_INT, -MAX_INT), (MAX_INT, 0), (-MAX_INT, MAX_INT), (MAX_INT, -1)
    )
