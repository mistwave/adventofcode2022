
xs = []
buf = 0

with open("input", "r") as f: 
    for line in f.readlines():
        l = line.strip()
        if l == "":
            xs.append(buf)
            buf = 0
        else:
            buf += int(l)

print("part 1:", max(xs))

print("part 2:", sum(sorted(xs, reverse=True)[:3]))



