#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def optimal_matchups(levels: list[int]) -> int:
    seq = sorted(levels)  # sorted; no need to abs() the differences
    n: int = len(seq)
    if n < 2:
        return 0

    # Easy case: even number of players
    if n % 2 == 0:
        return sum(seq[i + 1] - seq[i] for i in range(0, n, 2))

    # Hard case: odd number of players
    left_sum: int = 0
    right_sum: int = sum(seq[i + 1] - seq[i] for i in range(1, n, 2))
    result = left_sum + right_sum
    # Note: it's always better to remove an even index (todo: prove)
    for i in range(2, n, 2):
        left_sum += seq[i - 1] - seq[i - 2]
        right_sum -= seq[i] - seq[i - 1]
        result = min((result, left_sum + right_sum))
    return result
