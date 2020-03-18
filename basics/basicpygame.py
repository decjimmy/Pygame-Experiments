import pygame

pygame.init()

# initialize window
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

# Variable initialization
x = 50
y = 50
width = 40
height = 60
vel = 5

run = True

# Main Game Loop
while run:
    pygame.time.delay(100)  # Delay in Milliseconds

    for event in pygame.event.get(): #Loops through all events
        if event.type == pygame.QUIT: #checks for red x button
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        pass
    if keys[pygame.K_RIGHT]:
        pass
    if keys[pygame.K_UP]:
        pass
    if keys[pygame.K_DOWN]:
        pass

    pygame.draw.rect(win, (255,9,9), (x,y, width, height))
    pygame.display.update()
pygame.quit()

