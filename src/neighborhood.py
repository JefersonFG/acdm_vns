# -*- coding: utf-8 -*-

import math
import itertools
import src.schedule as schedule_function


def first_improvement(current_solution: list, neighborhood: int) -> list:
    """Returns the first neighbor that shows improvement over the previous solution."""
    neighbor_generators = itertools.combinations(range(len(current_solution)), neighborhood + 2)
    original_makespan = schedule_function.get_makespan(current_solution)

    for neighbor_generator in neighbor_generators:
        neighbor = schedule_function.swap_processes(current_solution, neighbor_generator)
        neighbor_makespan = schedule_function.get_makespan(neighbor)

        if neighbor_makespan < original_makespan:
            return neighbor

    return current_solution


def best_improvement(current_solution: list, neighborhood: int) -> list:
    """Checks the values of every neighbor and returns the one with the best improvement."""
    neighbor_generators = itertools.combinations(range(len(current_solution)), neighborhood + 2)
    best_neighbor = []

    original_makespan = schedule_function.get_makespan(current_solution)
    minimum_makespan = math.inf

    for neighbor_generator in neighbor_generators:
        neighbor = schedule_function.swap_processes(current_solution, neighbor_generator)
        neighbor_makespan = schedule_function.get_makespan(neighbor)

        if neighbor_makespan < minimum_makespan:
            minimum_makespan = neighbor_makespan
            best_neighbor = neighbor

    if minimum_makespan < original_makespan:
        return best_neighbor
    else:
        return current_solution


def neighborhood_change(current_solution: list, improvement_candidate: list, current_neighborhood: int) -> tuple:
    """Checks if the candidate improves upon the current solution and returns the new solution and neighborhood."""
    current_makespan = schedule_function.get_makespan(current_solution)
    candidate_makespan = schedule_function.get_makespan(improvement_candidate)

    new_solution = improvement_candidate
    new_neighborhood = 0

    if candidate_makespan >= current_makespan:
        new_solution = current_solution
        new_neighborhood = current_neighborhood + 1

    return new_solution, new_neighborhood
