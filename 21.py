import aoc
from functools import cache
from itertools import permutations


kpos = {
    '7':0+0j,
    '8':1+0j,
    '9':2+0j,
    
    '4':0+1j,
    '5':1+1j,
    '6':2+1j,
    
    '1':0+2j,
    '2':1+2j,
    '3':2+2j,

    '0':1+3j,
    'A':2+3j,
}

dpos = {
    '^':1,
    'A':2,

    '<':0+1j,
    'v':1+1j,
    '>':2+1j,
}


@cache
def permuts(chars:str):
    return {
        ''.join(perm)
        for perm in permutations(chars)
    }


@cache
def isOK(forbid:complex, p:complex, seq:str):
    for c in seq:
        p += {'<':-1,'>':1,'^':-1j,'v':1j}[c]
        if p == forbid: return False
    return True


@cache
def sublen(p:complex, code:str):
    if code == '': return 0
    v = code[0]
    n = dpos[v]
    dx = int(n.real - p.real)
    dy = int(n.imag - p.imag)
    return abs(dx) + abs(dy) + 1 + sublen(n, code[1:])


@cache
def subshortest(level:int,p:complex,code:str):
    if code == '': return 0
    
    v = code[0]
    n = dpos[v]
    
    dx = int(n.real - p.real)
    dy = int(n.imag - p.imag)
    moves = ('<' if dx < 0 else '>') * abs(dx) + ('^' if dy < 0 else 'v') * abs(dy)

    return min(
        sublen(dpos['A'], permut + 'A') if level == 2 else subshortest(level-1, dpos['A'], permut + 'A')
        for permut in permuts(moves)
        if isOK(0j, p, permut)
    ) + subshortest(level, n, code[1:])


@cache
def shortest(level:int,p:complex,code:str):
    if code == '': return 0
    
    v = code[0]
    n = kpos[v]

    dx = int(n.real - p.real)
    dy = int(n.imag - p.imag)
    moves = ('<' if dx < 0 else '>') * abs(dx) + ('^' if dy < 0 else 'v') * abs(dy)

    return min(
        subshortest(level, dpos['A'], permut + 'A')
        for permut in permuts(moves)
        if isOK(3j, p, permut)
    ) + shortest(level, n, code[1:])
   

def solve(text: str):
    lines = text.strip().split('\n')

    print(sum(int(code[:-1]) * shortest(2,kpos['A'], code) for code in lines))
    print(sum(int(code[:-1]) * shortest(25,kpos['A'], code) for code in lines))


example = '''
029A
980A
179A
456A
379A
'''
# solve(example)
solve(aoc.input_data())