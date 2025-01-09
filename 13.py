import aoc


def solve(text: str):
    chunks = text.strip().split('\n\n')
    tot = tot2 = 0

    for chunk in chunks:
        lines = chunk.split('\n')
        ax,ay = aoc.ints(lines[0])
        bx,by = aoc.ints(lines[1])
        gx,gy = aoc.ints(lines[2])
        best = 1e10
        for a in range(101):
            for b in range(101):
                if ax*a + bx*b == gx and ay*a + by*b == gy:
                    if a + b < best:
                        best = 3*a + b
        if best < 1e10: tot += best

        gx += 10000000000000
        gy += 10000000000000

        m_b = ax*by-bx*ay
        if m_b != 0:
            b = (ax*gy-ay*gx)/m_b
            if ax != 0:
                a = (gx-b*bx)/ax
                if a == int(a) and b == int(b): tot2 += int(3*a+b)

    print(tot,tot2)


example = '''
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
'''
# solve(example)
solve(aoc.input_data())