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
basicL = [ScreenImg(f"dancing_motion/basicL/img/11zon_{i}.jpeg") for i in range(1,13+1)]
basicR = [ScreenImg(f"dancing_motion/basicR/img/11zon_{i}.jpeg") for i in range(1,12+1)]
motion1L = [ScreenImg(f"dancing_motion/motion1L/img/11zon_{i}.jpeg") for i in range(1,12+1)]
motion1R = [ScreenImg(f"dancing_motion/motion1R/img/11zon_{i}.jpeg") for i in range(1,12+1)]
motion2L = [ScreenImg(f"dancing_motion/motion2L/img/11zon_{i}.jpeg") for i in range(5,15+1)]
motion2R = [ScreenImg(f"dancing_motion/motion2R/img/11zon_{i}.jpeg") for i in range(5,15+1)]
motion3L = [ScreenImg(f"dancing_motion/motion3L/img/11zon_{i}.jpeg") for i in range(1,6+1)]
motion3R = [ScreenImg(f"dancing_motion/motion3R/img/11zon_{i}.jpeg") for i in range(1,6+1)]
motion4L = [ScreenImg(f"dancing_motion/motion4L/img/11zon_{i}.jpeg") for i in range(1,6+1)]
motion4R = [ScreenImg(f"dancing_motion/motion4R/img/11zon_{i}.jpeg") for i in range(1,6+1)]
motion5L = [ScreenImg(f"dancing_motion/motion5L/img/11zon_{i}.jpeg") for i in range(1,64+1)]
motion5R = [ScreenImg(f"dancing_motion/motion5R/img/11zon_{i}.jpeg") for i in range(1,64+1)]
motion6L = [ScreenImg(f"dancing_motion/motion6L/img/11zon_{i}.jpeg") for i in range(1,6+1)]
motion6R = [ScreenImg(f"dancing_motion/motion6R/img/11zon_{i}.jpeg") for i in range(1,6+1)]
motion7L = [ScreenImg(f"dancing_motion/motion7L/img/11zon_{i}.jpeg") for i in range(1,12+1)]
motion7R = [ScreenImg(f"dancing_motion/motion7R/img/11zon_{i}.jpeg") for i in range(1,12+1)]
out = [ScreenImg(f"dancing_motion/out/img/11zon_{i}.jpeg") for i in range(1,44+1)]

#declare bgm ary
bgmAry = [["bgm/Usagi Flap.mp3", 124],
          ["bgm/Bunny Bunny Carrot Carrot.mp3", 113],
          ["bgm/After School Dessert.mp3", 121],
          ["bgm/Shooting Athletes.mp3", 118],
          ["bgm/Signal of Abydos.mp3", 113],
          ["bgm/NONE.mp3",None]]

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

txt1 = ScreenTxt("Press Space to Start!",pos_y = size_y /2 + 50)
txt2 = ScreenTxt("<change bgm by left and right key>",pos_y= size_y/2 + 80,size = 20)
txt3 = ScreenTxt("(select bgm)",pos_y = size_y / 2 - 50)
running1 = True
running2 = True
running3 = True
bgmType = 0
bgmName = bgmAry[bgmType][0][4:-4]
txt4 = ScreenTxt(bgmName,pos_y = size_y / 2 - 20,size = 25)

while(running1):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False

                screen.fill((0,0,0))
                pygame.display.update()

                music_start = time.time()
                running1 = False

            elif event.key == pygame.K_LEFT and bgmType > 0:
                bgmType -= 1
                bgmName = bgmAry[bgmType][0][4:-4]
                txt4.value = bgmName

            elif event.key == pygame.K_RIGHT and bgmType < len(bgmAry) - 1:
                bgmType += 1
                bgmName = bgmAry[bgmType][0][4:-4]
                txt4.value = bgmName

        elif event.type == pygame.QUIT:
            running1 = False
            running2 = False
            running3 = False

    screen.fill((0,0,0))
    txt1.show()
    txt2.show()
    txt3.show()
    txt4.show()
    pygame.display.update()

if (bgmAry[bgmType][1] != None):
    bgm = pygame.mixer.Sound(bgmAry[bgmType][0])
    bgm.set_volume(0.5)
    bgm.play()

dancingType = 1
toggle = False
isAlreadyOut = True
dType3Dir = 1 
dType6Dir = 1 
screen.fill((0,0,0))
pygame.display.update()

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

            elif event.key == pygame.K_7:
                dancingType = 7

            elif event.key == pygame.K_8:
                dancingType = 8

            elif event.key == pygame.K_SPACE:
                if not(isAlreadyOut):
                    toggle = 0
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
        
        elif dancingType == 6:
            left = motion5L
            right = motion5R
        
        elif dancingType == 7:
            left = motion6L
            right = motion6R

        elif dancingType == 8:
            left = motion7L
            right = motion7R

    #making arisu dancing
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                isAlreadyOut = False
                dancing(left)

                if dancingType == 3:
                    dType3Dir = 1
                
                elif dancingType == 6:
                    dType6Dir = 1
            
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:     
                isAlreadyOut = False      
                dancing(right)    

                if dancingType == 3:
                    dType3Dir = 0
                
                elif dancingType == 6:
                    dType6Dir = 0

            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                isAlreadyOut = False
                
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

        elif dancingType == 6:
            if dType6Dir:
                dancing(left)
            else:
                dancing(right)

        else:
            dancing(left)

            start = time.time()
            while(True):
                if time.time() - start > 0.02:
                    break

            dancing(right)

    if (bgmAry[bgmType][1] != None) and (time.time() - music_start >= bgmAry[bgmType][1]):
        if not(isAlreadyOut):
            dancing(out)
        
        running2 = False
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


