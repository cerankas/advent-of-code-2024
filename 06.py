import aoc


def solve(text: str):
    lines = text.strip().split('\n')
    rows = len(lines)
    cols = len(lines[0])
    p0 = None
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c == '^':
                p0 = [x,y]
    
    d = 0
    dd = [(0,-1),(1,0),(0,1),(-1,0)]
    x, y = p0
    positions = set()
    posdir = []
    while 1:
        positions.add((x,y))
        posdir.append((x,y,d))
        dx, dy = dd[d]
        nx, ny = x + dx, y + dy
        if not (0 <= nx < cols and 0 <= ny < rows):
            break
        if lines[ny][nx] == '#':
            d = (d + 1) % 4
            continue
        x, y = nx, ny

    print(len(positions))

    cnt = 0
    for xo,yo in positions:
        if lines[yo][xo] == '^': continue
        x, y = p0
        d = 0
        bumped = 0
        posdir = set()
        while 1:
            if bumped:
                if (x,y,d) in posdir:
                    cnt += 1
                    break
                posdir.add((x,y,d))

            dx, dy = dd[d]
            nx, ny = x + dx, y + dy
            if not (0 <= nx < cols and 0 <= ny < rows):
                break
            if nx == xo and ny == yo:
                bumped = 1
                d = (d + 1) % 4
                continue
            if lines[ny][nx] == '#':
                d = (d + 1) % 4
                continue
            x, y = nx, ny

    print(cnt)


example = '''
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
'''
# solve(example)
solve(aoc.input_data())