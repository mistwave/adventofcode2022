# solve file for day10 problem
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from read_file import by_lines

solve_dir = path.dirname(path.abspath(__file__))
input_path = path.join(solve_dir, "input")
content = by_lines(input_path)
testcontent = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".split(
    "\n"
)

# generated by make_dirs.py


class CRT:
    def __init__(self):
        self.buf = [" " for _ in range(240)]
        self.pp = 0

    def draw(self, ch: str):
        self.buf[self.pp] = ch
        self.pp = (self.pp + 1) % 240

    def show(self):
        for i in range(6):
            print("".join(self.buf[40 * i : 40 * (i + 1)]))


def solve() -> tuple[int, CRT]:
    res = 0
    pc = 0
    busy_cycle = 0
    running = 0
    x = 1
    cycle = 1

    crt = CRT()
    crt_pointer = 0

    while pc < len(content):
        # start of the cycle
        if busy_cycle == 0:
            op = content[pc]
            pc += 1
            if op.startswith("addx"):
                running = int(op.split(" ")[-1])
                busy_cycle = 1

        else:
            busy_cycle -= 1

        # draw
        if x - 1 <= crt_pointer <= x + 1:
            crt.draw('#')
        else:
            crt.draw('.')
        crt_pointer = (crt_pointer + 1) % 40

        # during the cycle
        if cycle % 40 == 20:
            res += cycle * x

        # end of cycle
        if busy_cycle == 0:
            x += running
            running = 0
        
        cycle += 1

    return res, crt


if __name__ == "__main__":
    p1, crt = solve()
    print("part1", p1)
    print("part2")
    crt.show()