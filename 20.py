import aoc
from collections import deque, defaultdict


def solve(text: str, limit1:int, limit2):
    lines = text.strip().split('\n')
    m = dict()
    for y,line in enumerate(lines):
        for x,c in enumerate(line):
            p = x + 1j*y
            m[p] = c
            if c == 'S': start = p
            if c == 'E': end = p

    def find_dist(p0):
        used = set()
        times = dict()
        qq = deque([(0,p0)])
        while qq:
            t,p = qq.popleft()
            if p in used: continue
            used.add(p)
            times[p] = t
            for d in (-1,1,-1j,1j):
                np = p + d
                if np in m and m[np] != '#':
                    qq.append((t+1,np))
        return times


    sdist = find_dist(start)
    edist = find_dist(end)

    time0 = sdist[end]

    cnt = 0
    hist = defaultdict(int)
    for cheat in m:
        if m[cheat] != '#': continue
        for d1 in (-1,1,-1j,1j):
            n1 = cheat + d1
            if n1 not in sdist: continue
            for d2 in (-1,1,-1j,1j):
                if d1 == d2: continue
                n2 = cheat + d2
                if n2 not in edist: continue
                t = sdist[n1] + edist[n2] + 2
                if t + limit1 <= time0:
                    cnt += 1
                    hist[time0 - t] += 1
            
    if limit2 < 100:
        for t in sorted(hist): print(f'{hist[t]}:{t} ',end='')
    print(cnt)

    length = 20
    cnt = 0
    hist = defaultdict(int)
    for c1 in sdist:
        for cx in range(int(c1.real-length),int(c1.real+length+1)):
            for cy in range(int(c1.imag-length),int(c1.imag+length+1)):
                c2 = cx + 1j * cy
                if c2 not in edist: continue
                dist = int(abs(c1.real-c2.real)+abs(c1.imag-c2.imag))
                if dist > length: continue
                t = sdist[c1] + edist[c2] + dist
                if t + limit2 <= time0:
                    cnt += 1
                    hist[time0 - t] += 1
    if limit2 < 100:
        for t in sorted(hist): print(f'{hist[t]}:{t} ',end='')
    print(cnt)


example = '''
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
'''
# solve(example,1,50)
solve(aoc.input_data(),100,100)