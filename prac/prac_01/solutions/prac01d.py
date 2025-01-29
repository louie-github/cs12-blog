#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from arya import Point, triangle_area


def cross(x1: int, y1: int, x2: int, y2: int) -> int:
    """Vector cross product (copied from arya)"""
    return x1 * y2 - x2 * y1


def is_on_line(a: Point, b: Point, p: Point):
    """
    Use a vector cross product to check if point p lies on the line
    segment from a to b.
    """
    return (
        sorted((a[0], b[0], p[0]))[1] == p[0]  # p.x is in bounds
        and sorted((a[1], b[1], p[1]))[1] == p[1]  # p.y is in bounds
        and cross(p[0] - a[0], p[1] - a[1], b[0] - a[0], b[1] - a[1]) == 0
    )


def is_in_triangle(A: Point, B: Point, C: Point, P: Point):
    # Degenerate case: all points coincide; check if on that point
    if A == B == C:
        return P == A
    # Degenerate case: points form a line; check if on that line
    for p1, p2, p3 in ((A, B, C), (A, C, B), (B, C, A)):
        if is_on_line(p1, p2, p3):
            return is_on_line(p1, p2, P)
    # General case: triangle area formula works
    return triangle_area(A, B, C) == (
        triangle_area(A, B, P) + triangle_area(B, C, P) + triangle_area(C, A, P)
    )
