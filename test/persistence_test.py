# -*- coding: utf-8 -*-

from src.persistence import *


def test_read_input():
    """Test that the read input function correctly return the list of process lengths."""
    test_input_data = "5\n1\n2\n3\n4\n5\n6\n7\n"
    test_input_path = ".persistence_test_tmp.dat"

    with open(test_input_path, 'w') as file:
        file.write(test_input_data)

    expected_output = [1, 2, 3, 4, 5]
    returned_output = read_input(test_input_path)

    os.remove(test_input_path)

    assert returned_output == expected_output


def test_log_step():
    """Test that the logger correctly logs the search info."""
    process_list = [1, 2, 3]
    schedule = [0, 1, 3]
    value = 6

    expected_line = "Makespan: 6 - Schedule: [0, 1, 3] - Process list: [1, 2, 3]"

    with Logger(cleanup=True) as persistence:
        persistence.log_step(process_list, schedule, value)

        with open(persistence.log_file, 'r') as file:
            lines = file.read().splitlines()
            assert lines[-1] == expected_line
