# -*- coding: utf-8 -*-

import random


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


def swap_processes(process_list: list, indexes: tuple) -> list:
    """Changes the process execution order by swapping k processes and generating a new schedule."""
    k = len(indexes)
    for i in range(k - 1):
        process_list[indexes[i]], process_list[indexes[i + 1]] = process_list[indexes[i + 1]], process_list[indexes[i]]

    return process_list


def shake_solution(process_list: list, shake_length: int) -> list:
    """Uses a pseudo random number generator to swap k values on the current solution."""
    num_processes = len(process_list)
    indexes = random.sample(range(num_processes), shake_length)
    return swap_processes(process_list, indexes)


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
