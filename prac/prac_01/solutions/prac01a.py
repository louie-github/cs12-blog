#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def who_gets_the_star(m: int, w: int, p: int, s: int) -> str:
    distances = {
        "MARIO": abs(s - m),
        "WIGI": abs(s - w),
        "PEARL": abs(s - p),
    }
    rankings = sorted(distances.keys(), key=lambda v: distances[v])
    if distances[rankings[0]] == distances[rankings[1]]:
        return "NONE"
    else:
        return rankings[0]
