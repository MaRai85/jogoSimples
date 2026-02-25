import pygame

pygame.init()

print('Setup Start')
window = pygame.display.set_mode(size=(600, 480))
print('Setup Finished')

print('Loop Start')
while True:
    """check for all events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()  # end pygame
