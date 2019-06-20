# -*- coding: utf-8 -*-

import random
import src.helper as helper


def get_schedule(process_list: list) -> list:
    """Generate a process schedule in the order processes were given, minimizing the time between them."""
    schedule = [0]

    for i in range(1, len(process_list)):
        current_length = process_list[i]
        minimum_start_list = []

        for j in range(i):
            previous_start = schedule[j]
            previous_length = process_list[j]
            min_length = min(current_length, previous_length)

            minimum_start_list.append(previous_start + min_length)

        schedule.append(max(minimum_start_list))

    return schedule


def swap_two_processes(process_list: list, indexes: tuple) -> list:
    """Changes the process execution order by swapping two processes and generating a new schedule."""
    i, j = indexes
    process_list[i], process_list[j] = process_list[j], process_list[i]

    return process_list


def swap_three_processes(process_list: list, indexes: tuple) -> list:
    """Changes the process execution order by swapping three processes and generating a new schedule."""
    i, j, k = indexes
    process_list[i], process_list[j], process_list[k] = process_list[j], process_list[k], process_list[i]

    return process_list


def shake_solution(process_list: list) -> list:
    """Uses a pseudo random number generator to swap k values on the current solution."""
    k = 4
    num_processes = len(process_list)

    helper.set_random_seed()
    index1, index2, index3, index4 = random.sample(range(num_processes), k)

    process_list[index1], process_list[index2], process_list[index3], process_list[index4] =\
        process_list[index4], process_list[index3], process_list[index2], process_list[index1]

    return process_list


def get_makespan(process_list: list) -> int:
    """Calculates the final makespan of the process schedule."""
    num_processes = len(process_list)
    makespan = 0

    schedule = get_schedule(process_list)

    for i in range(num_processes):
        current_span = process_list[i] + schedule[i]

        if current_span > makespan:
            makespan = current_span

    return makespan
