import pygame
import time
import sys
import random
pygame.init()

def fill_gradient(surface, color, gradient, rect=None, vertical=True, forward=True):
    """fill a surface with a gradient pattern
    Parameters:
    color -> starting color
    gradient -> final color
    rect -> area to fill; default is surface's rect
    vertical -> True=vertical; False=horizontal
    forward -> True=forward; False=reverse
    
    Pygame recipe: http://www.pygame.org/wiki/GradientCode
    """
    if rect is None: rect = surface.get_rect()
    x1,x2 = rect.left, rect.right
    y1,y2 = rect.top, rect.bottom
    if vertical: h = y2-y1
    else:        h = x2-x1
    if forward: a, b = color, gradient
    else:       b, a = color, gradient
    rate = (
        float(b[0]-a[0])/h,
        float(b[1]-a[1])/h,
        float(b[2]-a[2])/h
    )
    fn_line = pygame.draw.line
    if vertical:
        for line in range(y1,y2):
            color = (
                min(max(a[0]+(rate[0]*(line-y1)),0),255),
                min(max(a[1]+(rate[1]*(line-y1)),0),255),
                min(max(a[2]+(rate[2]*(line-y1)),0),255)
            )
            fn_line(surface, color, (x1,line), (x2,line))
    else:
        for col in range(x1,x2):
            color = (
                min(max(a[0]+(rate[0]*(col-x1)),0),255),
                min(max(a[1]+(rate[1]*(col-x1)),0),255),
                min(max(a[2]+(rate[2]*(col-x1)),0),255)
            )
            fn_line(surface, color, (col,y1), (col,y2))

class button():
    def __init__(self,color,x,y,xs,ys):
        pygame.draw.rect(self,color,(x,y,xs,ys))
        color2 = (41,0,102)
        pygame.draw.rect(self,color2,(x+10,y+10,xs-20,ys-20))

#####

size = [1250,750]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Insert name of file here")
nyan = pygame.image.load("Nyan-Cat-PNG.PNG").convert_alpha()
pygame.mouse.set_visible(True)

flag = False

clock = pygame.time.Clock()
fill_gradient(screen,(200, 255, 255), (255, 255, 255))
screen.blit(nyan,(250,250))
a = button.__init__(screen,(178,102,255),1150,15,85,80)
i = 100

while flag == False:

    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    fill_gradient(screen,(200, 255, 255), (255, 255, 255))
    if 1160+85 > mouse[0] > 1140 and 5 + 80 > mouse[1] > 25:
        a = button.__init__(screen,(128,52,195),1150,15,85,80)
        if click[0] == 1:
            print("Nyan")
            i = (i+100)%200
            screen.blit(nyan,(250,150+i))
        else:
            screen.blit(nyan,(250,250))
    else:
        a = button.__init__(screen,(178,102,255),1150,15,85,80)
        screen.blit(nyan,(250,250))
    pygame.display.update()
    clock.tick(15)
    

pygame.quit()
