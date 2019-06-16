# -*- coding: utf-8 -*-

from src.helper import *


def test_set_random_seed():
    """Checks that the random seed is set once, if it set twice the same number will be generated."""
    set_random_seed()
    a = random.randint(0, 10)

    set_random_seed()
    b = random.randint(0, 10)

    assert a != b
