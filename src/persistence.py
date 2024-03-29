# -*- coding: utf-8 -*-

import datetime
import os


def read_input(input_file_path) -> list:
    """Reads the input file and returns the list of process lengths."""
    process_list = []

    with open(input_file_path, 'r') as file:
        lines = file.read().splitlines()
        num_processes = int(lines[0])

        for i in range(num_processes):
            process_list.append(int(lines[i+1]))

    return process_list


class Logger:
    def __init__(self, cleanup=False):
        """Setups the log file with the current datetime, avoiding conflicts."""
        self.log_file = ("search_log_{}.csv".format(datetime.datetime.now()))
        open(self.log_file, 'a').close()

        self.cleanup = cleanup

    def __enter__(self):
        return self

    def log_step(self, value: int, time: float, output=False):
        """Writes the current solution and time run to reach it on csv format."""
        log_line = str(value) + ',' + str(time) + '\n'

        with open(self.log_file, 'a') as file:
            file.write(log_line)

        if output:
            print("Makespan: " + str(value) + " - Time run: " + str(time))

    def __exit__(self, exc_type, exc_value, traceback):
        """Removes the log file from persistence, used on tests."""
        if self.cleanup:
            os.remove(self.log_file)
