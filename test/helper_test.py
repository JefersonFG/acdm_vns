# -*- coding: utf-8 -*-

import src.helper as helper


def str2bool_test():
    """Checks that the conversion function accepts different boolean representations."""
    assert helper.str2bool("1")
    assert not helper.str2bool("0")

    assert helper.str2bool("true")
    assert not helper.str2bool("false")

    assert helper.str2bool("True")
    assert not helper.str2bool("False")

    assert helper.str2bool("t")
    assert not helper.str2bool("f")

    assert helper.str2bool("T")
    assert not helper.str2bool("F")
