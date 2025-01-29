#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from prac01a import who_gets_the_star


def test_who_gets_the_star():
    assert who_gets_the_star(4, 9, 1, 7) == "WIGI"
    assert who_gets_the_star(5, 9, 1, 7) == "NONE"

    # Batch 1: clear winners (no duplicate values)
    assert who_gets_the_star(2, 3, 4, 0) == "MARIO"
    assert who_gets_the_star(2, 3, 4, -2) == "MARIO"
    assert who_gets_the_star(-1, 3, -4, -2) == "MARIO"
    assert who_gets_the_star(2, 0, 4, -2) == "WIGI"
    assert who_gets_the_star(-1, 0, 3, 4) == "PEARL"

    # Batch 2: duplicate second place
    assert who_gets_the_star(-1, 0, -3, -2) == "NONE"
