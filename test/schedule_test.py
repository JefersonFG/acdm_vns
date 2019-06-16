# -*- coding: utf-8 -*-

from src.schedule import *


def check_solution_is_valid(process_list: list, solution: list):
    """Checks that a solution is valid according to the problem rules."""
    num_processes = len(solution)

    for i in range(num_processes - 1):
        for j in range(i + 1, num_processes):
            start_i = solution[i]
            start_j = solution[j]
            length_i = process_list[i]
            length_j = process_list[j]

            difference = abs(start_j - start_i)
            min_length = min(length_i, length_j)

            assert difference >= min_length


def test_get_schedule():
    """Checks that the get schedule function returns the correct times for the processes."""
    process_list = [1, 2, 4, 1, 3]
    expected_solution = [0, 1, 3, 4, 6]

    solution = get_schedule(process_list)

    check_solution_is_valid(process_list, solution)
    assert solution == expected_solution


def test_swap_two_processes():
    """Checks that the process swap keeps the solution valid."""
    process_list = [1, 2, 4, 1, 3]

    expected_process_list = [2, 1, 4, 1, 3]
    expected_schedule = [0, 1, 2, 3, 5]

    swapped_list = swap_two_processes(process_list, (0, 1))
    swapped_schedule = get_schedule(swapped_list)

    check_solution_is_valid(swapped_list, swapped_schedule)
    assert swapped_list == expected_process_list
    assert swapped_schedule == expected_schedule


def test_swap_three_processes():
    """Checks that the process swap keeps the solution valid."""
    process_list = [1, 2, 4, 1, 3]

    expected_process_list = [1, 1, 4, 3, 2]
    expected_schedule = [0, 1, 2, 5, 7]

    swapped_list = swap_three_processes(process_list, (1, 3, 4))
    swapped_schedule = get_schedule(swapped_list)

    check_solution_is_valid(swapped_list, swapped_schedule)
    assert swapped_list == expected_process_list
    assert swapped_schedule == expected_schedule


def test_shake_solution():
    """Checks that the shake is deterministic."""
    process_list = [1, 2, 4, 1, 3]

    expected_process_list = [2, 1, 4, 3, 1]
    expected_schedule = [0, 1, 2, 5, 6]

    shaken_process_list = shake_solution(process_list)
    shaken_schedule = get_schedule(shaken_process_list)

    check_solution_is_valid(shaken_process_list, shaken_schedule)
    assert shaken_process_list == expected_process_list
    assert shaken_schedule == expected_schedule


def test_get_makespan():
    """Checks that the makespan is correctly determined."""
    process_list = [1, 2, 4, 1, 3]
    expected_solution = 9

    makespan = get_makespan(process_list)
    assert makespan == expected_solution
