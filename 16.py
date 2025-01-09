import aoc


def solve(text: str):
    lines = text.strip().split('\n')

    free = set()
    for y,line in enumerate(lines):
        for x,c in enumerate(line):
            p = x + 1j * y
            if c != '#': free.add(p)
            if c == 'S': start = p
            if c == 'E': end = p

    dd = [1,1j,-1,-1j]

    nodes = set()
    for f in free:
        nn = sum(f+d in free for d in dd)
        if nn > 2:
            nodes.add(f)

    def spread(qq,end):
        best = 1e10
        dists = dict()
        visited = set()
        while qq:
            qq = sorted(qq, key=lambda q:q[0])
            score, p, d, path = qq.pop(0)

            if (p,d) in visited: continue
            visited.add((p,d))
            path = path | {p}
            
            if p == end and best > score:
                best = score

            if p in nodes:
                dists[p,d] = (score,path)

            np = p + dd[d]
            if np in free and (np,d) not in visited:
                qq.append((score+1, np, d, path))

            for nd in ((d-1)%4,(d+1)%4):
                if (p,nd) in visited: continue
                qq.append((score+1000, p, nd, path))

        return (dists, best)

    sdist, best = spread([(0,start,0,set())], end)
    edist, _ = spread([(0,end,0,set()), (0,end,1,set()), (0,end,2,set()), (0,end,3,set())], None)

    visited = set()
    for node in nodes:
        for d in range(4):
            sd,sp = sdist[node,d]
            ed,ep = edist[node,d]
            if sd + ed == best:
                visited |= sp | ep

    print(best, len(visited))


example = '''
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
'''
# solve(example)
solve(aoc.input_data())