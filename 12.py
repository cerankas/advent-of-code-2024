import aoc


def solve(text: str):
    lines = text.strip().split('\n')
    m = dict()
    for y,line in enumerate(lines):
        for x,c in enumerate(line):
            m[(x,y)] = c
    
    neig = ((-1,0),(1,0),(0,-1),(0,1))

    regions = []
    assigned = set()
    for x,y in m:
        if (x,y) in assigned: continue
        c = m[(x,y)]
        reg = set()
        qq = [(x,y)]
        while qq:
            qx,qy = qq.pop()
            if (qx,qy) in reg: continue
            reg.add((qx,qy))
            assigned.add((qx,qy))
            for dx,dy in neig:
                xx,yy = qx+dx,qy+dy
                if (xx,yy) not in m: continue
                if m[(xx,yy)] == c:
                    qq.append((xx,yy))
        regions.append(reg)
    
    price = 0
    for reg in regions:
        ar = pe = 0
        for x,y in reg:
            c = m[(x,y)]
            ar += 1
            for dx,dy in neig:
                xx,yy = x+dx,y+dy
                if (xx,yy) not in m or m[(xx,yy)] != c:
                    pe += 1
        price += ar * pe
    
    print(price)


def solve2(text: str):
    lines = text.strip().split('\n')
    m = dict()
    for y,line in enumerate(lines):
        for x,c in enumerate(line):
            m[(x,y)] = c
    
    neig = ((-1,0),(1,0),(0,-1),(0,1))

    regions = []
    assigned = set()
    for x,y in m:
        if (x,y) in assigned: continue
        c = m[(x,y)]
        reg = set()
        qq = [(x,y)]
        while qq:
            qx,qy = qq.pop()
            if (qx,qy) in reg: continue
            reg.add((qx,qy))
            assigned.add((qx,qy))
            for dx,dy in neig:
                nx,ny = qx+dx,qy+dy
                if (nx,ny) not in m: continue
                if m[(nx,ny)] == c:
                    qq.append((nx,ny))
        regions.append(reg)

    price = 0
    for reg in regions:
        ar = 0
        sides = []
        for x,y in reg:
            c = m[(x,y)]
            ar += 1
            for dx,dy in neig:
                nx,ny = x+dx,y+dy
                if (nx,ny) in m and m[(nx,ny)] == c: continue
                
                sx,sy = x+dx/2,y+dy/2
                if any((sx,sy) == p for side in sides for p in side): continue
                
                side = {(sx,sy)}
                
                i = 1
                while 1:
                    xx = x + dy * i
                    yy = y + dx * i
                    if (xx,yy) not in m or m[(xx,yy)] != c or ((xx+dx,yy+dy) in m and m[(xx+dx,yy+dy)] == c): break
                    side.add((xx+dx/2,yy+dy/2))
                    i += 1
                
                i = -1
                while 1:
                    xx = x + dy * i
                    yy = y + dx * i
                    if (xx,yy) not in m or m[(xx,yy)] != c or ((xx+dx,yy+dy) in m and m[(xx+dx,yy+dy)] == c): break
                    side.add((xx+dx/2,yy+dy/2))
                    i -= 1

                sides.append(side)
        
        pr = ar * len(sides)
        price += pr
    
    print(price)


example = '''
AAAA
BBCD
BBCC
EEEC
'''
ex2 = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""
ex3 = """
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
"""

# solve(example)
# solve(ex2)
solve(aoc.input_data())

# solve2(example)
# solve2(ex3)
solve2(aoc.input_data())