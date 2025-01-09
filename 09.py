import aoc


def solve(text: str):
    t = text.strip()

    disk = []
    for i,d in enumerate(t):
        disk += [-1 if i%2 else i // 2] * int(d)

    i = 0
    while i < len(disk):
        if disk[i] != -1:
            i += 1
            continue
        disk[i] = disk.pop()

    tot = 0
    for i,d in enumerate(disk):
        tot += i * d
    print(tot)


    disk = []
    for i,d in enumerate(t):
        disk += [-1 if i%2 else i // 2] * int(d)

    spaces = {i:0 for i in range(10)}
    end = len(disk) - 1
    while end > 0:
        if disk[end] == -1:
            end -= 1
            continue
        l = 1
        while end - l >= 0 and disk[end - l] == disk[end]:
            l += 1
        
        for i in range(spaces[l], end):
            if all(disk[i+j] == -1 for j in range(l)):
                for j in range(l):
                    disk[i+j] = disk[end-j]
                    disk[end-j] = -1
                spaces[l] = i
                break
        end -= l

    tot = 0
    for i,d in enumerate(disk):
        tot += i * d if d != -1 else 0
    print(tot)


# solve('2333133121414131402')
solve(aoc.input_data())