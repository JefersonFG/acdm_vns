# -*- coding: utf-8 -*-


from copy import deepcopy
from timeit import default_timer as timer
import src.schedule as schedule
import src.neighborhood as neighborhood
import src.persistence as persistence


def vns(current_solution: list, num_neighborhoods: int, max_time: int) -> list:
    """Implementation of VNS algorithm, runs until max_time is reached."""
    logger = persistence.Logger()
    time_elapsed = 0

    logger.log_step(current_solution, schedule.get_schedule(current_solution),
                    schedule.get_makespan(current_solution), True)

    while time_elapsed < max_time:
        start_time = timer()
        current_neighborhood = 0
        while current_neighborhood < num_neighborhoods:
            candidate_solution = schedule.shake_solution(deepcopy(current_solution))
            candidate_solution = neighborhood.best_improvement(candidate_solution, current_neighborhood)
            current_solution, current_neighborhood = neighborhood.neighborhood_change(current_solution,
                                                                                      candidate_solution,
                                                                                      current_neighborhood)

            if current_solution == candidate_solution:
                logger.log_step(current_solution, schedule.get_schedule(current_solution),
                                schedule.get_makespan(current_solution), True)

        time_elapsed += timer() - start_time

    return current_solution
