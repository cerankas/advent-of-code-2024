# Part 2 takes ~10 minutes to execute

import aoc


def solve(text: str):
    inputs,lines = text.strip().split('\n\n')
    inp = {}
    for line in inputs.split('\n'):
        n,v = line.split(': ')
        inp[n]=int(v)
    lin = {}    
    for line in lines.split('\n'):
        a,o,b,_,c = line.split()
        lin[c] = (a,o,b)
    
    while any(n.startswith('z') for n in lin):
        for n,(a,o,b) in lin.items():
            if a in inp and b in inp:
                va,vb = inp[a],inp[b]
                match o:
                    case 'OR': v = va | vb
                    case 'AND': v = va & vb
                    case 'XOR': v = va ^ vb
                    case _: print('missing',o,n)
                inp[n] = v
                del lin[n]
                break
    r = [inp[n] for n in sorted(inp.keys()) if n.startswith('z')]
    print(int(''.join(str(v) for v in r[::-1]),2))


def solve2(text: str):
    _,lines = text.strip().split('\n\n')
    gates = {}
    for line in lines.split('\n'):
        a,o,b,_,c = line.split()
        gates[c] = (a,o,b)
    
    nbits = sum(wire.startswith('x') for wire in set(w for a,_,b in gates.values() for w in (a,b)))

    val = {}
    def set_xy(x:int,y:int):
        for i in range(nbits):
            val[f'x{i:>02}'] = 1 if x & (1<<i) else 0
            val[f'y{i:>02}'] = 1 if y & (1<<i) else 0

    def get_wire(n,used=set()):
        if n in used: raise ValueError
        if n in val:
            return val[n]
        a,o,b = gates[n]
        uu = used | {n}
        a,b = get_wire(a,uu),get_wire(b,uu)
        match o:
            case 'OR': v = a | b
            case 'AND': v = a & b
            case 'XOR': v = a ^ b
        return v
    
    def check_add(x,y):
        set_xy(x,y)
        try: return x+y == int(''.join([str(get_wire(f'z{i:>02}')) for i in range(nbits+1)][::-1]),2)
        except: return False

    check_add_triple = lambda x,y: check_add(x,y) and check_add(x,0) and check_add(0,y)

    check_one_bit = lambda i: check_add_triple( 1<<i, 1<<i )

    check_all_bits = lambda: all(check_one_bit(i) for i in range(nbits))

    swapped = []

    def swap(a,b):
        gates[a],gates[b] = gates[b],gates[a]
        if a in swapped:
            swapped.remove(a)
            swapped.remove(b)
        else:
            swapped.append(a)
            swapped.append(b)

    wires_for_testing = list(gates)

    def find_swaps():
        checks = [check_one_bit(i) for i in range(nbits)]

        if sum(checks) == nbits:
            print(','.join(sorted(swapped)))
            return True

        if len(swapped) >= 8: return False

        found = []
        for i,c in enumerate(checks):
            if c: continue
            z = f'z{i:>02}'
            if z in swapped: continue
            for a in wires_for_testing:
                if z in swapped: continue
                swap(z,a)
                if check_one_bit(i):
                    if (ss := sum(check_one_bit(j) for j in range(nbits))) > sum(checks):
                        found.append((ss,z,a))
                swap(z,a)
        
        found = sorted(found,reverse=True)
        for _,a,b in found:
            swap(a,b)
            if find_swaps(): return True
            swap(a,b)

        if len(swapped) < 6: return False
        
        for na,a in enumerate(wires_for_testing):
            if a in swapped: continue
            for b in wires_for_testing[na+1:]:
                if b in swapped: continue
                swap(a,b)
                if check_all_bits():
                    if find_swaps(): return True
                swap(a,b)
        
        return False
        
    find_swaps()


example = '''
x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02
'''
# solve(example)
solve(aoc.input_data())
solve2(aoc.input_data())