import aoc


def solve(text: str):
    pieces = text.strip().split('\n\n')
    locks = []
    keys = []
    for piece in pieces:
        lines = piece.split()
        islock = lines[0] == "#####"
        if not islock: lines = lines[::-1]
        hh = [0,0,0,0,0]
        for h,line in enumerate(lines):
            for x,c in enumerate(line):
                if c == '#': hh[x] = h
        
        if islock:
            locks.append(hh)
        else:
            keys.append(hh)

    cnt = 0
    for ll in locks:
        for kk in keys:
            if all(l+k <= 5 for l,k in zip(ll,kk)): cnt += 1

    print(cnt)


example = '''
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
'''
# solve(example)
solve(aoc.input_data())