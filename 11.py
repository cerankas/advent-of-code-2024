import aoc
from functools import cache


@cache
def num(n:int,b:int):
    if b == 0: return 1
    if n == 0: return num(1,b-1)
    s = str(n)
    if len(s) % 2 == 0:
        l = len(s) // 2
        return num(int(s[:l]),b-1) + num(int(s[l:]),b-1)
    else:
        return num(n*2024,b-1)
    

def solve(text: str, blinks:int):
    nn = aoc.ints(text.strip())

    print(sum(num(n,blinks) for n in nn))
    return
    

# solve('0 1 10 99 999',1)
# solve('125 17',25)
solve(aoc.input_data(),25)
solve(aoc.input_data(),75)