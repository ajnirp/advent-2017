with open('4.txt', 'r') as f:
    res = 0
    for line in f.readlines():
        l = line.strip().split()
        w = set(l)
        if len(w) == len(l):
            res += 1
    print(res)

with open('4.txt', 'r') as f:
    res = 0
    for line in f.readlines():
        l = line.strip().split()
        w = set([''.join(sorted(w)) for w in l])
        # w = set(sorted(w) for w in l)
        if len(w) == len(l):
            res += 1
    print(res)