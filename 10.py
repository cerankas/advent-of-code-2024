import aoc


def solve(text: str):
    grid = text.strip().split('\n')
    rows = len(grid)
    cols = len(grid[0])

    dir = ((-1,0),(1,0),(0,1),(0,-1))

    d = dict()

    for x in range(cols):
        for y in range(rows):
            if grid[y][x] == '9':
                d[(x,y,9)] = {(x,y)}

    tot = 0
    for n in range(8,-1,-1):
        nd = n + 1
        digit = chr(ord('0') + n)
        for x in range(cols):
            for y in range(rows):
                if grid[y][x] != digit: continue
                found = set()
                for dx,dy in dir:
                    nx, ny = x+dx, y+dy
                    if (nx,ny,nd) in d:
                        found |= d[(nx,ny,nd)]
                if found:
                    d[x,y,n] = found
                if n == 0:
                    tot += len(found)
    print(tot)


    d = dict()

    for x in range(cols):
        for y in range(rows):
            if grid[y][x] == '9':
                d[(x,y,9)] = {(x,y)}

    tot = 0
    for n in range(8,-1,-1):
        nd = n + 1
        digit = chr(ord('0') + n)
        for x in range(cols):
            for y in range(rows):
                if grid[y][x] != digit: continue
                found = set()
                for dx,dy in dir:
                    nx, ny = x+dx, y+dy
                    if (nx,ny,nd) in d:
                        found |= {(x,y,*trail) for trail in d[(nx,ny,nd)]}
                if found:
                    d[x,y,n] = found
                if n == 0:
                    tot += len(found)
    print(tot)


example = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
# solve(example)
solve(aoc.input_data())