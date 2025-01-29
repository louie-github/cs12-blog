#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from prac01a import who_gets_the_star


def test_who_gets_the_star():
    assert who_gets_the_star(4, 9, 1, 7) == "WIGI"
    assert who_gets_the_star(5, 9, 1, 7) == "NONE"

    # TODO add more tests
