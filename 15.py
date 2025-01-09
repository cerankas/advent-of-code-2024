import aoc


def solve(text: str):
    field, commands = text.strip().split('\n\n')
    commands = commands.replace('\n','')

    walls = set()
    boxes = set()
    for y,line in enumerate(field.split('\n')):
        for x,c in enumerate(line):
            xy = x + 1j * y
            if c == '#':
                walls.add(xy)
            if c == 'O':
                boxes.add(xy)
            if c == '@': 
                robot = xy

    for command in commands:
        delta = {'<':-1, '>':1, '^':-1j, 'v':1j}[command]
        moved_robot = robot + delta
        if moved_robot in walls: continue
        if moved_robot in boxes:
            moved_box = moved_robot
            while moved_box in boxes:
                moved_box += delta
            if moved_box in walls: continue
            boxes.remove(moved_robot)
            boxes.add(moved_box)
        robot = moved_robot

    print(int(sum(box.real + 100 * box.imag for box in boxes)))


    walls = set()
    boxes = set()
    for y,line in enumerate(field.split('\n')):
        for x,c in enumerate(line):
            xy = 2*x + 1j * y
            if c == '#':
                walls.add(xy)
                walls.add(xy+1)
            if c == 'O':
                boxes.add((xy,xy+1))
            if c == '@': 
                robot = xy

    for command in commands:
        delta = {'<':-1, '>':1, '^':-1j, 'v':1j}[command]
        moved_robot = robot + delta
        if moved_robot in walls: continue

        blocked = False
        for box in boxes:
            if moved_robot in box:
                to_check = {box}
                moved_from = set()
                moved_to = set()
                
                while to_check:
                    box = to_check.pop()
                    moved_box = tuple(xy + delta for xy in box)
                
                    if any(xy in walls for xy in moved_box):
                        moved_from = set()
                        break
                
                    moved_from.add(box)
                    moved_to.add(moved_box)
                    to_check |= {
                        another_box for another_box in boxes 
                            if box != another_box 
                            if any(xy == another_xy 
                                for xy in moved_box
                                for another_xy in another_box)}
                
                if not moved_from:
                    blocked = True
                    break
                
                boxes -= moved_from
                boxes |= moved_to
                break
        
        if not blocked:
            robot = moved_robot
            
    print(int(sum(box[0].real + 100 * box[0].imag for box in boxes)))


example = '''
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
'''
# solve(example)
solve(aoc.input_data())