# solve file for day04 problem 
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from read_file import by_lines
solve_dir = path.dirname(path.abspath(__file__))
input_path = path.join(solve_dir, "input")
content = by_lines(input_path)

# generated by make_dirs.py
