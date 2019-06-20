# -*- coding: utf-8 -*-


import argparse
import src.persistence as persistence
import src.schedule as schedule
import src.vns as vns


parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str, help='File containing the process list')

args = parser.parse_args()
initial_process_list = persistence.read_input(args.input_file)

time_limit = 60
num_neighborhoods = 2

solution = vns.vns(initial_process_list, num_neighborhoods, time_limit)

print("Best solution:\n")
print("Makespan: {}".format(schedule.get_makespan(solution)))
print("Schedule: {}".format(schedule.get_schedule(solution)))
print("Process list: {}".format(solution))
