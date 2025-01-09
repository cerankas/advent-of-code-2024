import aoc
from collections import defaultdict


def solve(text: str):
    tot = 0
    seqs = defaultdict(int)

    for s in aoc.ints(text):
        pp = []
        used = set()
    
        for _ in range(2000):
            s = ((s * 64) ^ s) % 16777216
            s = ((s // 32) ^ s) % 16777216
            s = ((s * 2048) ^ s) % 16777216
            
            p = s % 10
            pp.append(p)
            if len(pp) > 4:
                seq = (pp[-4]-pp[-5], pp[-3]-pp[-4], pp[-2]-pp[-3], pp[-1]-pp[-2])
                if seq not in used:
                    used.add(seq)
                    seqs[seq] += p
        
        tot += s
    
    print(tot, max(seqs.values()))


example = '''
1
10
100
2024
'''
example2 = '''
1
2
3
2024
'''
# solve(example)
# solve(example2)
solve(aoc.input_data())