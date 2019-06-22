# -*- coding: utf-8 -*-

from src.helper import *


def str2bool_test():
    """Checks that the conversion function accepts different boolean representations."""
    assert str2bool("1")
    assert not str2bool("0")

    assert str2bool("true")
    assert not str2bool("false")

    assert str2bool("True")
    assert not str2bool("False")

    assert str2bool("t")
    assert not str2bool("f")

    assert str2bool("T")
    assert not str2bool("F")
