# -*- coding: utf-8 -*-

from copy import deepcopy
from timeit import default_timer as timer
from src.schedule import get_makespan, shake_solution
from src.neighborhood import best_improvement, first_improvement, neighborhood_change
from src.persistence import Logger


def vns(current_solution: list, num_neighborhoods: int, max_time: int,
        use_best_improvement: bool, shake_length: int, max_iterations: int) -> list:
    """Implementation of VNS algorithm, runs until max_time is reached."""
    logger = Logger()
    time_limit = timer() + max_time
    time_elapsed = 0
    iterations = 1

    logger.log_step(get_makespan(current_solution), time_elapsed, True)

    while time_elapsed < max_time:
        current_neighborhood = 0
        while current_neighborhood < num_neighborhoods and time_elapsed < max_time:
            start_time = timer()
            remaining_time = time_limit - start_time

            candidate_solution = shake_solution(deepcopy(current_solution), shake_length)

            if use_best_improvement:
                candidate_solution = best_improvement(candidate_solution, current_neighborhood,
                                                      remaining_time)
            else:
                candidate_solution = first_improvement(candidate_solution, current_neighborhood,
                                                       remaining_time)

            current_solution, current_neighborhood = neighborhood_change(current_solution,
                                                                         candidate_solution,
                                                                         current_neighborhood)

            time_elapsed += timer() - start_time

            if current_solution == candidate_solution:
                logger.log_step(get_makespan(current_solution), time_elapsed, True)
            else:
                iterations += 1
                if iterations == max_iterations:
                    iterations = 1
                    current_neighborhood += 1

    return current_solution
