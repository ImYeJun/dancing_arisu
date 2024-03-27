import pygame
import time

size_x = 600
size_y = 338

screen = pygame.display.set_mode((size_x,size_y))

#load img,easy to show
class ScreenImg:
    def __init__(self,value = None, pos_x = size_x/2, pos_y = size_y/2, pos_central = True):
        self.value = value
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_central = pos_central

        if pos_central == True:
            self.object = pygame.image.load(value)
            self.pos_object = self.object.get_rect()
            self.pos_object.center = (self.pos_x,self.pos_y)

        elif pos_central == False:
            self.object = pygame.image.load(value)
            self.pos_object =  self.object.get_rect()
            self.pos_object.x = self.pos_x
            self.pos_object.y = self.pos_y
               
    def show(self):
        self.value = self.value
        self.pos_x = self.pos_x
        self.pos_y = self.pos_y

        if self.pos_central == True:
            self.object = pygame.image.load(self.value)
            self.pos_object = self.object.get_rect()
            self.pos_object.center = (self.pos_x,self.pos_y)

        elif self.pos_central == False:
            self.object = pygame.image.load(self.value)
            self.pos_object =  self.object.get_rect()
            self.pos_object.x = self.pos_x
            self.pos_object.y = self.pos_y

        if self.pos_central == True:
            screen.blit(self.object,self.pos_object)
        elif self.pos_central == False:
            screen.blit(self.object,self.pos_object)

test = [f"C:/Users/user/Desktop/아리스 뿜뿜/basicL/img/11zon_{i}.jpeg" for i in range(1,13+1)]


for i in range(0,13):
    test[i].show()
    time.sleep(0.01)