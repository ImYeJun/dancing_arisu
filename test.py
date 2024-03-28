import pygame

pygame.init()

size_x = 338
size_y = 338

screen = pygame.display.set_mode((size_x,size_y))
pygame.display.set_caption("Dancing Arisu!")
pygame_icon = pygame.image.load("icon.png")
pygame.display.set_icon(pygame_icon)

pygame.scrap.init()
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                print(str(pygame.scrap.get(pygame.SCRAP_TEXT))[2:-1])