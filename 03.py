import aoc


def solve(text: str):
    def eat(n):
        nonlocal text
        text = text[n:]

    tot = tot2 = 0
    enabled = True
    while text:
        if text.startswith('do()'):
            enabled = True

        if text.startswith('don\'t()'):
            enabled = False

        if not text.startswith('mul('):
            eat(1)
            continue
        eat(4)

        f = ''
        while text and '0' <= text[0] <= '9':
            f += text[0]
            eat(1)
        if not (1 <= len(f) <= 3):
            continue
        a = int(f)
        if text[0] != ',':
            continue
        
        eat(1)

        f = ''
        while text and '0' <= text[0] <= '9':
            f += text[0]
            eat(1)
        if not (1 <= len(f) <= 3):
            continue
        b = int(f)
        if text[0] != ')':
            continue

        tot += a * b

        if enabled:
            tot2 += a * b

    print(tot, tot2)


# solve("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
# solve("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
solve(aoc.input_data())