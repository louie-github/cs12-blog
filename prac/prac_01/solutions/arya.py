#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fractions import Fraction

Point = tuple[int, int]  # type alias

def triangle_area(a: Point, b: Point, c: Point) -> Fraction:
    return abs(cross(*a, *b) + cross(*b, *c) + cross(*c, *a)) / Fraction(2)

def cross(x1: int, y1: int, x2: int, y2: int) -> int:
    return x1 * y2 - x2 * y1
