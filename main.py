import pygame
import time
pygame.init()

size_x = 338
size_y = 338

screen = pygame.display.set_mode((size_x,size_y))
pygame.display.set_caption("Dancing Arisu!")
pygame_icon = pygame.image.load("icon.png")
pygame.display.set_icon(pygame_icon)

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

#create txt object
class ScreenTxt:
    def __init__(self,value = None, pos_x = size_x/2, pos_y = size_y/2, pos_central = True,font = None,size = 30,txt_color = (255,255,255),txt_background = None,bold = False, italic = False,antialias= True):
        self.value = value
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_central = pos_central
        self.txt_color = txt_color
        self.txt_background = txt_background
        self.bold = bold
        self.antialias = antialias
        self.font = pygame.font.Font(font,size)

        if pos_central == True:
            self.object = self.font.render(value,antialias,txt_color)
            self.pos_object = self.object.get_rect()
            self.pos_object.center = (self.pos_x,self.pos_y)
        
        elif pos_central == False:
            self.object = self.font.render(value,antialias,txt_color)
            self.pos_object =  self.object.get_rect()
            self.pos_object.x = self.pos_x
            self.pos_object.y = self.pos_y
    
    def show(self):
            self.value = self.value
            self.pos_x = self.pos_x
            self.pos_y = self.pos_y
            self.pos_central = self.pos_central
            self.txt_color = self.txt_color
            self.txt_background = self.txt_background
            self.bold = self.bold
            self.antialias = self.antialias
            self.pos_central = self.pos_central
            
            if self.pos_central == True:
                self.object = self.font.render(self.value,self.antialias,self.txt_color)
                self.pos_object = self.object.get_rect()
                self.pos_object.center = (self.pos_x,self.pos_y)
            
            elif self.pos_central == False:
                self.object = self.font.render(self.value,self.antialias,self.txt_color)
                self.pos_object =  self.object.get_rect()
                self.pos_object.x = self.pos_x
                self.pos_object.y = self.pos_y

            if self.pos_central == True:

                screen.blit(self.object,self.pos_object)
            elif self.pos_central == False:
                screen.blit(self.object,self.pos_object)

#declare img ary
basicL = [ScreenImg(f"basicL/img/11zon_{i}.jpeg") for i in range(1,13+1)]
basicR = [ScreenImg(f"basicR/img/11zon_{i}.jpeg") for i in range(1,12+1)]
motion1L = [ScreenImg(f"motion1L/img/11zon_{i}.jpeg") for i in range(1,12+1)]
motion1R = [ScreenImg(f"motion1R/img/11zon_{i}.jpeg") for i in range(1,12+1)]
motion2L = [ScreenImg(f"motion2L/img/11zon_{i}.jpeg") for i in range(5,15+1)]
motion2R = [ScreenImg(f"motion2R/img/11zon_{i}.jpeg") for i in range(5,15+1)]
motion3L = [ScreenImg(f"motion3L/img/11zon_{i}.jpeg") for i in range(1,6+1)]
motion3R = [ScreenImg(f"motion3R/img/11zon_{i}.jpeg") for i in range(1,6+1)]
motion4L = [ScreenImg(f"motion4L/img/11zon_{i}.jpeg") for i in range(1,6+1)]
motion4R = [ScreenImg(f"motion4R/img/11zon_{i}.jpeg") for i in range(1,6+1)]
motion5 = [ScreenImg(f"motion5/img/11zon_{i}.jpeg") for i in range(1,64+1)]
out = [ScreenImg(f"out/img/11zon_{i}.jpeg") for i in range(1,44+1)]

usagiFlap = pygame.mixer.Sound("usagi flap.mp3")
usagiFlap.set_volume(0.5)

def dancing(ary):   
    if ary == None:
        pass

    else:
        frame = len(ary)
        for i in range(0,frame):
            start = time.time()
            
            ary[i].show()
            pygame.display.update()

            while(True):
                if (time.time()- start) > 0.03:
                    break

txt1 = ScreenTxt("Press Any Key to Start!")
txt1.show()
pygame.display.update()

running1 = True
running2 = True
running3 = True

while(running1):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            running = False

            screen.fill((0,0,0))
            pygame.display.update()

            usagiFlap.play()
            music_start = time.time()
            running1 = False

        elif event.type == pygame.QUIT:
            running1 = False
            running2 = False
            running3 = False

dancingType = 1
toggle = False
isAlreadyOut = False
dType3Dir = 1

while(running2):
    #select dancing type
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                dancingType = 1

            elif event.key == pygame.K_2:           
                dancingType = 2

            elif event.key == pygame.K_3:
                dancingType = 3
        
            elif event.key == pygame.K_4:
                dancingType = 4

            elif event.key == pygame.K_5:
                dancingType = 5

            elif event.key == pygame.K_6:
                dancingType = 6

            elif event.key == pygame.K_SPACE:
                isAlreadyOut = True
                dancing(out)

        #stop arisu dancing    
        elif event.type == pygame.QUIT:
            if not(isAlreadyOut):
                dancing(out)

            running2 = False
            running3 = False
    
    #select left,right motion by dancingType variable
        if dancingType == 1:
            left = basicL
            right = basicR
        
        elif dancingType == 2:
            left = motion1L
            right = motion1R
        
        elif dancingType == 3:
            left = motion2L
            right = motion2R

        elif dancingType == 4:
            left = motion3L
            right = motion3R

        elif dancingType == 5:
            left = motion4L
            right = motion4R
        
        #need more frame
        elif dancingType == 6:
            left = motion5
            right = motion5

    #making arisu dancing
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                isAlreadyOut = False
                dancing(left)

                if dancingType == 3:
                    dType3Dir = 1
            
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:     
                isAlreadyOut = False      
                dancing(right)    

                if dancingType == 3:
                    dType3Dir = 0

            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if toggle:
                    toggle = False
                else:
                    toggle = True

    if toggle:
        if dancingType == 3:
            if dType3Dir:
                dancing(left)
            else:
                dancing(right)

        else:
            dancing(left)

            if dancingType != 6:
                start = time.time()
                while(True):
                    if time.time() - start > 0.02:
                        break

                dancing(right)

    if (time.time() - music_start >= 123.5):
        dancing(out)
        running2 = False

running = True
screen.fill((0,0,0))
txt2 = ScreenTxt("End!")
txt2.show()
pygame.display.update()

while(running3):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running3 = False
        
        elif event.type == pygame.KEYDOWN:
            running3 = False