import pygame
import sys

# initializing the constructor
pygame.init()
# screen resolution
res = (720,720)
# opens up a window
screen = pygame.display.set_mode(res)
# white color
color = (255,255,255)
# light shade of the button
color_light = (170,170,170)
# dark shade of the button
color_dark = (100,100,100)
# stores the width of the
# screen into a variable
width = screen.get_width()
# stores the height of the
# screen into a variable
height = screen.get_height()
# defining a font
smallfont = pygame.font.SysFont('Corbel',30)
bigfont = pygame.font.SysFont('Corbel',50)

running = True

class Scene(object):
    def __init__(self):
        pass

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError

class SceneManager(object):
    def __init__(self):
        self.go_to(MenuScreen())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self

class TitleScreen(Scene):
    def __init__(self):
        super(TitleScreen, self).__init__()
        self.bg = Surface(res)
        self.bg.fill((60,25,60))
        
    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError

class MenuScreen(Scene):
    def __init__(self):
        super(MenuScreen, self).__init__()
        self.font = bigfont
        self.sfont = smallfont

    def render(self, screen):
        # color screen
        self.bg = Surface(res)
        self.bg.fill((60,25,60))
        # screen.fill((60,25,60))

        # standard quit rectangle
        quitrectStd = pygame.draw.rect(screen,color_dark,[width/2-70,height/2,140,40])

        # quit text for button
        quitText = smallfont.render('quit' , True , color)

        # centering quit text
        quittext_rect = quitText.get_rect()
        quittext_rect.center = quitrectStd.center

        # superimposing the text onto the button
        screen.blit(quitText , quittext_rect)

    def update(self):
        pass

    def handle_events(self, events):
        for ev in pygame.event.get():
        
            if ev.type == pygame.QUIT:
                pygame.quit()
            #checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
            
                #if the mouse is clicked on the
                # button the game is terminated
                if width/2-70 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                    pygame.quit()

        # if mouse is hovered on a button it
        # changes to lighter shade
        if width/2-70 <= mouse[0] <= width/2+70 and height/2 <= mouse[1] <= height/2+40:
            quitrectHover = pygame.draw.rect(screen,color_light,[width/2-70,height/2,140,40])

def main():    

    manager = SceneManager()

    while running:
                    
        # fills the screen with a color
        screen.fill((60,25,60))
        
        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        # if pygame.event.get(QUIT):
        #     running = False
        #     return

        manager.scene.handle_events(pygame.event.get())
        manager.scene.update()
        manager.scene.render(screen)
        pygame.display.update()
        # updates the frames of the game