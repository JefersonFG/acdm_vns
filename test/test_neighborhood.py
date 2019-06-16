# -*- coding: utf-8 -*-

from src.neighborhood import *


def test_first_improvement():
    """Checks that the first improvement function returns the first best solution."""
    process_list = [1, 2, 4, 1, 3]
    expected_solution = [2, 1, 4, 1, 3]

    first_solution = first_improvement(process_list, NEIGHBORHOOD_LIST[0])
    assert first_solution == expected_solution


def test_best_improvement():
    """Checks that the best improvement function checks all possible solutions and returns the best."""
    process_list = [1, 2, 4, 1, 3]
    expected_solution = [3, 1, 4, 2, 1]

    best_solution = best_improvement(process_list, NEIGHBORHOOD_LIST[0])
    assert best_solution == expected_solution


def test_neighborhood_change():
    """Checks that the neighborhood is correctly changed only when no improvement was made."""
    current_solution = [1, 2, 4, 1, 3]
    improvement_candidate = [2, 1, 4, 1, 3]
    current_neighborhood = 0

    expected_solution = [2, 1, 4, 1, 3]
    expected_neighborhood = 0

    new_solution, new_neighborhood = neighborhood_change(current_solution, improvement_candidate, current_neighborhood)

    assert new_solution == expected_solution
    assert new_neighborhood == expected_neighborhood

    current_solution = [1, 2, 4, 1, 3]
    improvement_candidate = [1, 2, 4, 1, 3]
    current_neighborhood = 0

    expected_solution = [1, 2, 4, 1, 3]
    expected_neighborhood = 1

    new_solution, new_neighborhood = neighborhood_change(current_solution, improvement_candidate, current_neighborhood)

    assert new_solution == expected_solution
    assert new_neighborhood == expected_neighborhood
