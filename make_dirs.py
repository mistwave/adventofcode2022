import os

# replace your token
AOC_COOKIE = os.environ["AOC_COOKIE"]

def make_dirs(maxnum: int):
    for i in range(1, maxnum+1):
        # create dir
        dirname = f"day{i:02}"
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        else:
            print(f"ingored: {dirname} existed")
        # make solve file
        solvefilename = f"{dirname}/solve.py"
        if not os.path.isfile(solvefilename):
            with open(solvefilename, "w") as f:
                f.write(f"# solve file for day{i:02} problem ")
        else:
            print(f"ingored: {solvefilename} existed")
        # download input
        inputfilename = f"{dirname}/input"
        if not os.path.isfile(inputfilename):
            content = get_input(i)
            with open(inputfilename, "w") as f:
                f.write(content)
        else:
            print(f"ingored: {inputfilename} existed")

        print(f"======done for problem {i:02}")


def get_input(i: int) -> str:
    import httpx

    url = f"https://adventofcode.com/2022/day/{i}/input"

    headers = {
        "cookie": AOC_COOKIE
    }

    r = httpx.get(url, headers=headers)
    return r.text


if __name__ == "__main__":
    from sys import argv
    if len(argv) < 2:
        print("please input number of issue")
    else:
        make_dirs(int(argv[1]))
