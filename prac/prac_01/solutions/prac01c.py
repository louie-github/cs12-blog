#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def all_permutations(
    done: frozenset[int] = frozenset(),
) -> list[list[int]]:
    if len(done) < 5:
        return [
            lst
            for i in range(0, 5)
            if i not in done
            for lst in ([i, *rest] for rest in all_permutations(done | {i}))
        ]
    else:
        return [[]]


def verify_weights(vals: list[int], c12: str, c23: str, c34: str, c45: str):
    return (
        (vals[0] < vals[1] if c12 == "<" else vals[0] > vals[1])
        and (vals[1] < vals[2] if c23 == "<" else vals[1] > vals[2])
        and (vals[2] < vals[3] if c34 == "<" else vals[2] > vals[3])
        and (vals[3] < vals[4] if c45 == "<" else vals[3] > vals[4])
    )


def queens(c12: str, c23: str, c34: str, c45: str) -> dict[int, list[int]]:
    retval: dict[int, list[int]] = {}
    for seq in all_permutations():
        if len(retval) == 5:
            break
        if not verify_weights(seq, c12, c23, c34, c45):
            continue
        for i in range(5):
            if i not in retval and seq.index(sorted(seq)[2]) == i:
                retval[i] = seq
    return {k + 1: [w + 1 for w in v] for k, v in retval.items()}


if __name__ == "__main__":
    for c12 in "<>":
        for c23 in "<>":
            for c34 in "<>":
                for c45 in "<>":
                    assert sorted(get_candidates(c12, c23, c34, c45)) == sorted(
                        queens(c12, c23, c34, c45).keys()
                    ), (get_candidates(c12, c23, c34, c45), queens(c12, c23, c34, c45))
