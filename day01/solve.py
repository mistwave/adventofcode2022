import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from read_file import by_lines

solve_dir = path.dirname(path.abspath(__file__))
input_path = path.join(solve_dir, "input")
content = by_lines(input_path)

xs = []
buf = 0


for line in content:
    l = line.strip()
    if l == "":
        xs.append(buf)
        buf = 0
    else:
        buf += int(l)

print("part 1:", max(xs))

print("part 2:", sum(sorted(xs, reverse=True)[:3]))



