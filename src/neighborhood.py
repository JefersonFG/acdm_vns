# -*- coding: utf-8 -*-

import math
import itertools
from timeit import default_timer as timer
from src.schedule import get_makespan, swap_processes


def first_improvement(current_solution: list, neighborhood: int, remaining_time: float) -> list:
    """Returns the first neighbor that shows improvement over the previous solution."""
    neighbor_generators = itertools.combinations(range(len(current_solution)), neighborhood + 2)
    original_makespan = get_makespan(current_solution)
    start_time = timer()

    for neighbor_generator in neighbor_generators:
        if timer() - start_time >= remaining_time:
            break

        neighbor = swap_processes(current_solution, neighbor_generator)
        neighbor_makespan = get_makespan(neighbor)

        if neighbor_makespan < original_makespan:
            return neighbor

    return current_solution


def best_improvement(current_solution: list, neighborhood: int, remaining_time: float) -> list:
    """Checks the values of every neighbor and returns the one with the best improvement."""
    neighbor_generators = itertools.combinations(range(len(current_solution)), neighborhood + 2)
    best_neighbor = []
    start_time = timer()

    original_makespan = get_makespan(current_solution)
    minimum_makespan = math.inf

    for neighbor_generator in neighbor_generators:
        if timer() - start_time >= remaining_time:
            break

        neighbor = swap_processes(current_solution, neighbor_generator)
        neighbor_makespan = get_makespan(neighbor)

        if neighbor_makespan < minimum_makespan:
            minimum_makespan = neighbor_makespan
            best_neighbor = neighbor

    if minimum_makespan < original_makespan:
        return best_neighbor
    else:
        return current_solution


def neighborhood_change(current_solution: list, improvement_candidate: list, current_neighborhood: int) -> tuple:
    """Checks if the candidate improves upon the current solution and returns the new solution and neighborhood."""
    current_makespan = get_makespan(current_solution)
    candidate_makespan = get_makespan(improvement_candidate)

    new_solution = improvement_candidate
    new_neighborhood = 0

    if candidate_makespan >= current_makespan:
        new_solution = current_solution
        new_neighborhood = current_neighborhood + 1

    return new_solution, new_neighborhood
