#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def optimal_matchups(skill_levels: list[int]) -> int:
    sorted_levels = sorted(skill_levels)
    # Handle edge cases
    n: int = len(sorted_levels)
    if n < 2:  # no matchups
        return 0
    elif n == 2:
        return sorted_levels[1] - sorted_levels[0]

    if n % 2 == 0:
        # Technically, we don't need the abs(), but let's be safe.
        return sum(abs(sorted_levels[i + 1] - sorted_levels[i]) for i in range(0, n, 2))
    else:
        # Super slow, but let's optimize further later.
        min_sum = float("inf")
        for rem_i in range(n):
            new_levels = sorted_levels.copy()
            new_levels.pop(rem_i)
            min_sum = min(
                (
                    min_sum,
                    sum(
                        abs(new_levels[i + 1] - new_levels[i])
                        for i in range(0, n - 1, 2)
                    ),
                )
            )
        assert isinstance(min_sum, int)
        return min_sum
