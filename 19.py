import aoc
from functools import cache


def solve(text: str):
    lines = text.strip().split('\n')

    chunks = lines[0].split(', ')

    @cache
    def count_possible(design:str):
        return 1 if not design else sum(
            count_possible(design[len(chunk):]) 
            for chunk in chunks 
            if design.startswith(chunk)
        )

    designs = lines[2:]
    
    print(
        sum(count_possible(design) > 0 for design in designs), 
        sum(count_possible(design) for design in designs)
    )


example = '''
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
'''
# solve(example)
solve(aoc.input_data())