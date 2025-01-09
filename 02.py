import aoc


def solve(text: str):
    lines = text.strip().split('\n')

    def check(v):
        sortedv = tuple(sorted(v))
        order_ok = v == sortedv or v == sortedv[::-1]
        diffs = set(abs(a - b) for a, b in zip(v[1:],v[:-1]))
        diffs_ok = all(d in {1,2,3} for d in diffs)
        return order_ok and diffs_ok

    t,t2 = 0,0
    for line in lines:
        v = tuple(aoc.ints(line))
        if check(v):
            t += 1
            t2 += 1
            continue
        for i in range(len(v)):
            if check(v[:i] + v[i+1:]):
                t2 += 1
                break

    print(t,t2)


example = '''
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''
# solve(example)
solve(aoc.input_data())