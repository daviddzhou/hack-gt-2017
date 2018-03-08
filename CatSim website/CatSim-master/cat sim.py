import pygame
import time
import random
import sys

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

pygame.display.set_caption('Cat Simulator')

white = (255,255,255)
black = (0,0,0)
turquoise = (64,224,208)
purple = (178,102,255)
lightPurple = (128,52,195)
cyan = (200, 255, 255)

smallfont = pygame.font.Font('neuropol.ttf', 25)
medfont = pygame.font.Font('neuropol.ttf', 60)
largefont = pygame.font.Font('neuropol.ttf', 80)

def doraemon():

    dora = pygame.image.load("doraemon.png")
    pygame.mouse.set_visible(True)

    flag = False

    gameDisplay.blit(dora,(250,250))
    a = button.__init__(gameDisplay,purple,700,15,85,80)
    i = 100

    while flag == False:

        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        fill_gradient(gameDisplay,cyan,white)
        if 700+85 > mouse[0] > 700 and 15 + 80 > mouse[1] > 15:
            a = button.__init__(gameDisplay,lightPurple,700,15,85,80)
            if click[0] == 1:
                i = (i+100)%200
                gameDisplay.blit(dora,(250,150+i))
            else:
                gameDisplay.blit(dora,(250,250))
        else:
            a = button.__init__(gameDisplay,purple,700,15,85,80)
            gameDisplay.blit(dora,(250,250))
        pygame.display.update()
        clock.tick(10)
        

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


def text_objects(text, color,size = "small"):

    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)
   
def message_to_screen(msg,color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (int(display_width / 2), int(display_height / 2)+y_displace)
    gameDisplay.blit(textSurf, textRect)

class button():
    def __init__(self,color,x,y,xs,ys):
        pygame.draw.rect(self,color,(x,y,xs,ys))
        color2 = (41,0,102)
        pygame.draw.rect(self,color2,(x+10,y+10,xs-20,ys-20))    


def gameIntro():

    intro = True

    while intro:

        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        fill_gradient(gameDisplay,cyan,white)
        message_to_screen("Cat Simulation",turquoise,-100,size="large")
        message_to_screen("<3, CS-TA FIESTA",turquoise,-25)

        pygame.draw.rect(gameDisplay,black,(150,500,100,50))
        pygame.draw.rect(gameDisplay,black,(350,500,100,50))
        pygame.draw.rect(gameDisplay,black,(550,500,100,50))

        text_to_button("Start", turquoise, 150,500,100,50)
        text_to_button("Help", turquoise, 350,500,100,50)
        text_to_button("Load", turquoise, 550,500,100,50)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 150 < mouse[0] < 250 and 500 < mouse[1] < 550:
            s = pygame.Surface((100,50))
            s.set_alpha(150)
            s.fill((255,255,255))
            gameDisplay.blit(s,(150,500))
            if click[0] == 1:
                doraemon()
        pygame.display.update()

gameIntro()

##def startGame():
##
##    for evt in pygame.event.get():
##        if evt.type == pygame.QUIT:
##            pygame.quit()
##            sys.exit()
##    
##    mouse = pygame.mouse.get_pos()
##    print(mouse)
##    click = pygame.mouse.get_pressed()
##    if 150 < mouse[0] < 250 and 500 < mouse[1] < 550:
##        s = pygame.Surface((100,50))
##        s.set_alpha(255)
##        s.fill((255,255,255))
##        gameDisplay.blit(s,(150,500))
##        if click[0] == 1:
##            cat()
##
##    pygame.display.update()

pygame.quit()


            
