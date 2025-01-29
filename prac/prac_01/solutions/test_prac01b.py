#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pyright: strict

from prac01b import optimal_matchups


def test_optimal_matchups():
    assert optimal_matchups([1, 7, 2, 10, 4, 7]) == 7
    assert optimal_matchups([3, 1, 4]) == 1

    # Handle edge cases
    assert optimal_matchups([]) == 0
    for i in (1, 10, 100, 10**5, 10**10):
        assert optimal_matchups([i]) == 0
    assert optimal_matchups([1, 1]) == 0
    assert optimal_matchups([1, 2]) == 1
    assert optimal_matchups([2, 1]) == 1
    assert optimal_matchups([10**10, 1]) == 10**10 - 1
    assert optimal_matchups([1, 10**10]) == 10**10 - 1

    assert optimal_matchups([1, 2, 3]) == 1
    assert optimal_matchups([1, 2, 4]) == 1
    assert optimal_matchups([0, 2, 4]) == 2

    assert optimal_matchups([1, 2, 3, 4, 5]) == 2
    assert optimal_matchups([1, 2, 3, 4, 8]) == 2
    assert optimal_matchups([0, 2, 3, 4, 8]) == 3
    assert optimal_matchups([0, 1, 3, 4, 8]) == 2
    assert optimal_matchups([1, 4, 5, 6, 7]) == 2

    assert optimal_matchups([1, 2, 4, 9, 10, 11, 12]) == 3
