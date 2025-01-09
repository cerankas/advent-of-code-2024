import aoc


def solve(text: str):
    lines = text.strip().split('\n')

    nodes = set()
    links = set()
    for line in lines:
       a,b = line.split('-')
       links.add(frozenset((a,b)))
       nodes.add(a)
       nodes.add(b)

    are_connected = lambda a,b: frozenset((a,b)) in links

    triples = set()
    for n in nodes:
        if not n.startswith('t'): continue
        for a,b in links:
            if are_connected(a,n) and are_connected(b,n):
                triples.add(frozenset((a,b,n)))
    print(len(triples))

    nets = set()
    for n in nodes:
        if any(n in net for net in nets): continue
        gathered = {n}
        candidates = nodes.copy()
        while True:
            found = None
            for c in candidates:
                if all(are_connected(c,g) for g in gathered):
                    found = c
                    break
            if found:
                gathered.add(found)
                candidates.remove(found)
            else:
                break
        nets.add(frozenset(gathered))
    
    largest = sorted(nets,key=len)[-1]
    print(','.join(sorted(largest)))


example = '''
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
'''
# solve(example)
solve(aoc.input_data())