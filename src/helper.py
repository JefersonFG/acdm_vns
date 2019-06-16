# -*- coding: utf-8 -*-

import random


def run_once(f):
    """Decorator to guarantee f is only run once, returns None when f is called again."""
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper


@run_once
def set_random_seed():
    """Sets the random generator seed to a fixed one so the program is deterministic."""
    random.seed(184604)
