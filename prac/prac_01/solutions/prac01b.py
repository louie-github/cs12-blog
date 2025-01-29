#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def _prefix_sums(seq: list[int]):
    cur_sum = 0
    for i in seq:
        cur_sum += i
        yield cur_sum


def get_prefix_sums(seq: list[int]):
    return list(_prefix_sums(seq))


def _get_differences(seq: list[int]):
    for i in range(0, len(seq), 2):
        yield abs(seq[i] - seq[i + 1])


def get_differences(seq: list[int]) -> list[int]:
    return list(_get_differences(seq))


def optimal_matchups(skill_levels: list[int]) -> int:
    seq = sorted(skill_levels)
    # Handle edge cases
    n: int = len(seq)
    if n < 2:  # no matchups
        return 0
    elif n == 2:
        return seq[1] - seq[0]
    elif n == 3:
        return min(abs(seq[i1] - seq[i2]) for i1, i2 in ((1, 0), (2, 0), (2, 1)))
    if n % 2 == 0:
        return sum(get_differences(seq))
    else:
        assert n >= 5
        left_psums = get_prefix_sums(get_differences(seq[:-1]))
        right_psums = get_prefix_sums(get_differences(seq[::-1][:-1]))
        min_sum = float("inf")
        for ri in range(n):  # which index to simulate removing
            if ri == 0:
                cur_sum = right_psums[-1]
            elif ri == 1:
                cur_sum = abs(seq[2] - seq[0]) + right_psums[-2]
            elif ri == n - 2:
                cur_sum = left_psums[-2] + abs(seq[-1] - seq[-3])
            elif ri == n - 1:
                cur_sum = left_psums[-1]
            elif ri % 2 == 0:
                cur_sum = left_psums[ri // 2 - 1] + right_psums[-(ri // 2 + 1)]
            else:
                cur_sum = (
                    left_psums[ri // 2 - 1]
                    + (abs(seq[ri - 1] - seq[ri + 1]))
                    + right_psums[(-(ri + 1) // 2) - 1]
                )
            if cur_sum < min_sum:
                min_sum = cur_sum
        assert isinstance(min_sum, int)
        return min_sum
