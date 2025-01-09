import aoc


def run(ii:list[int], aa=None):
    a,b,c,*prog = ii

    if aa != None: a = aa

    out = []
    ptr = 0
    while 0 <= ptr < len(prog) - 1:
        jmp = None
        cmd = prog[ptr]
        lop = prog[ptr + 1]

        match lop:
            case 4: cop = a
            case 5: cop = b
            case 6: cop = c
            case 7: cop = 'inv'
            case _ as cop: pass
        
        match cmd & 7:
            case 0: a = a // 2**cop
            case 1: b = b ^ lop
            case 2: b = cop % 8
            case 3: jmp = lop if a else None
            case 4: b = b ^ c
            case 5: out += [cop % 8]
            case 6: b = a // 2**cop
            case 7: c = a // 2**cop
        
        ptr = jmp if jmp != None else ptr + 2
    
    return out


def solve(text: str):
    ii = aoc.ints(text)
    print(','.join(map(str,run(ii))))


def solve2(text: str):
    ii = aoc.ints(text)
    prog = ii[3:]

    def score(out):
        if len(out) != len(prog): return -1
        for n,(x,y) in enumerate(zip(reversed(out),reversed(prog))):
            if x != y: return n
        return len(out)
    
    a = 1
    while len(run(ii,a)) < len(prog): a *= 2

    delta = a
    while 1:
        delta //= 2  
        best = -1
        for aa in range(a - 500 * delta, a + 500 * delta, delta):
            sc = score(run(ii,aa)) if aa > 0 else -2
            if best < sc:
                best = sc
                a = aa
            if delta == 1 and sc == len(prog):
                print(aa)
                return


example = '''
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
'''
example2 = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""
# solve(example)
solve(aoc.input_data())
# solve2(example2)
solve2(aoc.input_data())