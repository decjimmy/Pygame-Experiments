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

pygame.quit()

