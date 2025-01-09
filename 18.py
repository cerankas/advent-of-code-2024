import aoc


def solve(text: str, span:int, amount:int):
    lines = text.strip().split('\n')
    bytes = list()
    for line in lines:
        x,y = aoc.ints(line)
        p = x + 1j*y
        bytes.append(p)
    
    end = span + 1j * span
    
    def travel_time(limit:int):
        qq = [(0,0j)]
        visited = set()
        while qq:
            t,p = qq.pop(0)
            if p == end:
                return t
            if p in visited: continue
            visited.add(p)
            for d in (-1,1,-1j,1j):
                n = p + d
                if n in visited: continue
                if n in bytes[:limit]: continue
                if not (0 <= n.real <= span and 0 <= n.imag <= span): continue
                qq.append((t+1,n))
        return 0

    print(travel_time(amount))
    
    l1 = 0
    l2 = len(bytes)
    n = 0
    while 1:
        n += 1
        l = (l1 + l2) // 2
        t = travel_time(l)
        if t:
            l1 = l
        else:
            l2 = l
        if l1 + 1 == l2:
            p = bytes[l1]
            print(f'{int(p.real)},{int(p.imag)}')
            break


example = '''
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
'''
# solve(example,6,12)
solve(aoc.input_data(),70,1024)