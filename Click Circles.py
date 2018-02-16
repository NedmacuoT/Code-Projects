import random
import pygame
pygame.init()

width = 600
height = 600
window = pygame.display.set_mode([width,height])


white = (255,255,255)
black = (0,0,0)
window.fill(white)

size = 15

def distance(x,y,c,u):
    dis = (((c - x) ** 2) + ((u - y) ** 2)) ** 0.5
    return(dis)
i = 0
l = 0
circles = [random.randint(size,width - size),random.randint(size,height - size)]
pygame.draw.circle(window,black,(circles[i],circles[i + 1]),size)
pygame.display.flip()
playing = True
on = False
color_change = False
color = ""
run = 0
color = black
color_width = 30
color_height = 30
track = 0
r = pygame.Rect(0,0,color_width,color_height)
colors = []
for v in range(int(width / color_width)):
    colors.append((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    
while playing:


    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        check = True
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            for z in range(int(len(circles) / 2)):
                x,y = pygame.mouse.get_pos()
                dist = distance(x,y,circles[l],circles[l + 1])
                if dist <= size:
                    on = True
                l += 2
            l = 0
            if on:
                
                circles.append(random.randint(size, width - size))
                circles.append(random.randint(size, height - size))
                i += 2
                
                
                pygame.draw.circle(window,color,(circles[i],circles[i + 1]),size)
            on = False
            for p in range(len(colors)):
                if y <= color_height:
                    if x > track and x < track + color_width:
                        color = colors[p]
                    track += color_width
            track = 0
                    
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            window.fill(white)
            color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            for q in range(int(len(circles)) // 2):
                pygame.draw.circle(window,color,(circles[run],circles[run + 1]),size)
                run += 2
            run = 0
    for a in range(len(colors)):
        pygame.draw.rect(window,colors[a],r)
        r.x += color_width
    r.x = 0
    pygame.display.flip()             
