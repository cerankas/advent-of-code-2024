import aoc


def solve(text: str):
    lines = text.strip().split('\n')

    rows = len(lines)
    cols = len(lines[0])

    w = 'XMAS'

    el = lambda x,y: lines[y][x]

    dd = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,1),(1,-1),(-1,1))

    cnt = 0
    for x in range(cols):
        for y in range(rows):
            for dx,dy in dd:
                if not 0 <= y + dy*(len(w)-1) < rows:
                    continue
                if not 0 <= x + dx*(len(w)-1) < cols:
                    continue
                if any(el(x+dx*i,y+dy*i) != c for i,c in enumerate(w)):
                    continue
                cnt += 1

    print(cnt)

    w = 'MAS'

    cnt = 0
    for x in range(cols-2):
        for y in range(rows-2):
            cc = 0
            for x0,y0,dx,dy in ((0,0,1,1),(0,2,1,-1),(2,0,-1,1),(2,2,-1,-1)):
                if all(el(x+x0+dx*i,y+y0+dy*i) == c for i,c in enumerate(w)):
                    cc += 1
            if cc == 2: cnt += 1

    print(cnt)


example = '''
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
'''
# solve(example)
solve(aoc.input_data())