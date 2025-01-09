import aoc


def solve(text: str):
    lines = text.strip().split('\n')
    
    rows = len(lines)
    cols = len(lines[0])

    d = dict()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '.': continue
            if c not in d:
                d[c] = {(x,y)}
            else:
                d[c].add((x,y))

    anti = set()
    anti2 = set()

    def add(x,y, an):
        if 0 <= x < cols and 0 <= y < rows:
            an.add((x,y))
            return 1
        return 0

    def add2(x,y,dx,dy):
        i = 0
        while add(x+dx*i,y+dy*i,anti2): 
            i += 1
        i = -1
        while add(x+dx*i,y+dy*i,anti2): 
            i -= 1
            
    for c in d:
        nodes = d[c]
        for a in nodes:
            xa, ya = a
            for b in nodes:
                if a == b: continue
                xb, yb = b
                dx, dy = xb-xa, yb-ya
                add(xa-dx,ya-dy,anti)
                add(xb+dx,yb+dy,anti)
                add2(xa,ya,dx,dy)
                
    print(len(anti), len(anti2))


example = '''
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
'''
# solve(example)
solve(aoc.input_data())