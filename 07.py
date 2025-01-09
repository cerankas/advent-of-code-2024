import aoc


def con(a:int, b:int):
    return int(str(a) + str(b))

def test(res, v, vv):
    if not vv:
        return res == v
    return test(res, v + vv[0], vv[1:]) or test(res, v * vv[0], vv[1:])

def test2(res, v, vv):
    if not vv:
        return res == v
    return test2(res, v + vv[0], vv[1:]) or test2(res, v * vv[0], vv[1:]) or test2(res, con(v, vv[0]), vv[1:])

def solve(text: str):
    lines = text.strip().split('\n')
    tot = tot2 = 0
    for line in lines:
        res, *v = aoc.ints(line)
        if test(res, v[0], v[1:]):
            tot += res
        if test2(res, v[0], v[1:]):
            tot2 += res

    print(tot, tot2)


example = '''
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
'''
# solve(example)
solve(aoc.input_data())