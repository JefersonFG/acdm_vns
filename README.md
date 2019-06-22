# ACDM VNS

Final project for the optimization class - UFRGS 2019/1

## Usage

```bash
usage: acdm_vns.py [-h]
                   output_file input_file [num_neighborhoods] [shake_length]
                   [use_best_improvement] [random_seed] [execution_time]

positional arguments:
  output_file           File on which to write the output
  input_file            File containing the process list
  num_neighborhoods     Number of neighborhoods to evaluate, default 2
  shake_length          Number of processes to swap on the shake process,
                        default 4
  use_best_improvement  Use best improvement on local search, if false or not
                        specified uses first improvement
  random_seed           Seed for the RNG, same seed and parameters wield the
                        same results, default 184604
  execution_time        Time for which to run the algorithm in seconds,
                        default 60

optional arguments:
  -h, --help            show this help message and exit
```

## Running the tests

You will need to install the nose package:

```bash
pip install nose
```

Then to run the tests from the root folder:

```bash
python test/test_runner.py
```
