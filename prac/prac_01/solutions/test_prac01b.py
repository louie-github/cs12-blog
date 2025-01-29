#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pyright: strict

import random
from prac01b import optimal_matchups


def reference(seq: list[int]) -> int:
    seq = sorted(seq)
    if len(seq) < 2:
        return 0
    elif len(seq) % 2 == 0:
        return sum(seq[i + 1] - seq[i] for i in range(0, len(seq), 2))
    else:
        result = float("inf")
        for i in range(len(seq)):
            ns = seq[:i] + seq[i + 1 :]
            result = min((result, sum(ns[i + 1] - ns[i] for i in range(0, len(ns), 2))))
        assert isinstance(result, int)
        return result


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


def test_randomly():
    for n in range(2, 15):
        for _ in range(1000):
            nums = [random.randint(1, 10**10) for _ in range(n)]
            assert optimal_matchups(nums) == reference(nums)
