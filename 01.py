import aoc


def solve(text: str):
    lines = text.strip().split('\n')
    tot = 0
    ii, jj = [], []
    for line in lines:
        i,j = aoc.ints(line)
        ii.append(i)
        jj.append(j)
    for i, j in zip(sorted(ii), sorted(jj)):
        tot += abs(i - j)

    tot2 = 0
    for i in ii:
        tot2 += i * len(list(1 for j in jj if j == i))
        
    print(tot, tot2)


example = '''
3   4
4   3
2   5
1   3
3   9
3   3
'''
# solve(example)
solve(aoc.input_data())