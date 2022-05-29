import pygame

# --- class ---

class Button(object):

    def __init__(self, position, size):

        # create 3 images
        self._images = [
            pygame.Surface(size),    
            pygame.Surface(size),    
            pygame.Surface(size),    
        ]

        # fill images with color - red, gree, blue
        self._images[0].fill((255,0,0))
        self._images[1].fill((0,255,0))
        self._images[2].fill((0,0,255))

        # get image size and position
        self._rect = pygame.Rect(position, size)

        # select first image
        self._index = 0

    def draw(self, screen):

        # draw selected image
        screen.blit(self._images[self._index], self._rect)

    def event_handler(self, event):
        # change selected color if rectange clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # is some button clicked
            if self._rect.collidepoint(event.pos): # is mouse over button
                self._index = (self._index+1) % 3 # change image

# --- main ---

# init        

pygame.init()

screen = pygame.display.set_mode((320,110))

# create buttons

button1 = Button((5, 5), (100, 100))

# mainloop

running = True

while running:

    # --- events ---

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # --- buttons events ---
        button1.event_handler(event)
    # --- draws ---
    button1.draw(screen)
    pygame.display.update()

# --- the end ---

pygame.quit()