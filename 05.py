import aoc


def solve(text: str):
    lines = text.strip().split('\n')
    rules = []
    tot = 0
    tot2 = 0
    for line in lines:
        if line == '': continue

        if '|' in line:
            rules.append(aoc.ints(line))
            continue

        pages = aoc.ints(line)
        bad = 0
        for a,b in rules:
            if a in pages and b in pages and pages.index(a) > pages.index(b):
                bad = 1
                break
        
        if not bad:
            tot += pages[len(pages) // 2]
            continue

        # bad

        while 1:
            moved = 0
            for a,b in rules:
                if a in pages and b in pages and pages.index(a) > pages.index(b):
                    moved += 1
                    ia = pages.index(a)
                    ib = pages.index(b)
                    pages[ia] = b
                    pages[ib] = a
            if moved == 0: break

        tot2 += pages[len(pages) // 2]

    print(tot, tot2)


example = '''
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
'''
# solve(example)
solve(aoc.input_data())