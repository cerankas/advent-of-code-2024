import aoc
import pygame
import numpy as np


def solve(text: str, wi:int, he:int):
    lines = text.strip().split('\n')
    rr = []
    for line in lines:
        x,y,dx,dy = aoc.ints(line)
        rr += [([x,y],(dx,dy))]

    for t in range(100):
        for p,d in rr:
            p[0] += d[0]
            p[1] += d[1]
            while p[0] <= 0: p[0] += wi
            while p[0] >= wi: p[0] -= wi
            while p[1] <= 0: p[1] += he
            while p[1] >= he: p[1] -= he
            
    q = [0,0,0,0]
    for (x,y),_ in rr:
        if x < wi//2:
            if y < he//2: q[0]+=1
            if y > he//2: q[1]+=1
        if x > wi//2:
            if y < he//2: q[2]+=1
            if y > he//2: q[3]+=1
    print(q[0]*q[1]*q[2]*q[3])


def solve2(text: str, wi:int, he:int):
    pix = 8
    pygame.init()
    win = pygame.display.set_mode((wi*pix, he*pix))

    def show_robots(rr:list[list[int,int]]):
        bitmap = np.zeros((wi,he), dtype=np.uint8)

        for x,y in rr:
            bitmap[x][y] = 255

        bitmap = np.repeat(np.repeat(bitmap, pix, axis=0), pix, axis=1)

        surface = pygame.surfarray.make_surface(np.stack([bitmap]*3, axis=-1))

        win.blit(pygame.transform.scale(surface, win.get_rect().size), (0, 0))
        pygame.display.flip()

    lines = text.strip().split('\n')
    rr = []
    for line in lines:
        x,y,dx,dy = aoc.ints(line)
        rr += [([x,y],(dx,dy))]

    states = []
    for t in range(wi*he):
        for p,d in rr:
            p[0] += d[0]
            p[1] += d[1]
            while p[0] <= 0: p[0] += wi
            while p[0] >= wi: p[0] -= wi
            while p[1] <= 0: p[1] += he
            while p[1] >= he: p[1] -= he
        states.append(tuple((x,y) for (x,y),_ in rr))
    
    t = max(list(range(len(states))), key=lambda t:len(set(states[t]))) + 1
    print(t)
    
    while 1:
        if 0 < t <= wi*he: show_robots(states[t-1])
        pygame.display.set_caption(str(t))
        while 1:
            dt = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP: dt -= 1
                    if event.key == pygame.K_DOWN: dt += 1
                    if event.key == pygame.K_PAGEUP: dt -= 101
                    if event.key == pygame.K_PAGEDOWN: dt += 101
            if dt:
                t += dt
                break


example = '''
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
'''
# solve(example,11,7)
solve(aoc.input_data(),101,103)
solve2(aoc.input_data(),101,103)