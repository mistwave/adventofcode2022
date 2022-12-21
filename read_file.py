from typing import List

def by_lines(path: str) -> List[str]:
    res = []
    with open(path, 'r') as f:
        for line in f.readlines():
            res.append(line.rstrip("\n"))

    return res


