# -*- coding: utf-8 -*-

import math
import random
import argparse
from src.persistence import read_input
from src.schedule import get_makespan, get_schedule
from src.vns import vns
from src.helper import str2bool


parser = argparse.ArgumentParser()

parser.add_argument('output_file', type=str, help='File on which to write the output')
parser.add_argument('input_file', type=str, help='File containing the process list')
parser.add_argument('num_neighborhoods', type=int, nargs='?', default=2,
                    help='Number of neighborhoods to evaluate, default 2')
parser.add_argument('shake_length', type=int, nargs='?', default=4,
                    help='Number of processes to swap on the shake process, default 4')
parser.add_argument('use_best_improvement', type=str2bool, nargs='?', default=False,
                    help='Use best improvement on local search, if false or not specified uses first improvement')
parser.add_argument('random_seed', type=int, nargs='?', default=184604,
                    help='Seed for the RNG, same seed and parameters wield the same results, default 184604')
parser.add_argument('execution_time', type=int, nargs='?', default=60,
                    help='Time for which to run the algorithm in seconds, default 60')
parser.add_argument('max_iterations', type=int, nargs='?', default=math.inf,
                    help='Maximum number of iterations between improvements, defaults to no limit')

args = parser.parse_args()

output_file = args.output_file
input_file = args.input_file
num_neighborhoods = args.num_neighborhoods
shake_length = args.shake_length
use_best_improvement = args.use_best_improvement
random_seed = args.random_seed
execution_time = args.execution_time
max_iterations = args.max_iterations

try:
    initial_process_list = read_input(input_file)
    random.seed(random_seed)

    solution = vns(initial_process_list, num_neighborhoods, execution_time,
                   use_best_improvement, shake_length, max_iterations)

    print("Best solution: {}\n".format(get_makespan(solution)))

    with open(output_file, 'w') as file:
        file.write("Best solution:\n\n")
        file.write("Makespan: {}\n".format(get_makespan(solution)))
        file.write("Schedule: {}\n".format(get_schedule(solution)))
        file.write("Process list: {}\n".format(solution))
except FileNotFoundError:
    print("Invalid input file")
