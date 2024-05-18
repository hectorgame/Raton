import pygame
import math

# Initialize Pygame
pygame.init()

# Set up some constants
screen_width = 800
screen_height = 600
background_color = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the clock
clock = pygame.time.Clock()

# Load the animal mouse image
animal_mouse = pygame.image.load('animal_mouse.png')

# Set up the cursor rect
cursor_rect = animal_mouse.get_rect()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Move the cursor to the mouse position
    cursor_rect.center = mouse_pos

    # Rotate the animal mouse image
    rotated_animal_mouse = pygame.transform.rotate(animal_mouse, math.degrees(pygame.time.get_ticks() / 100))

    # Draw everything
    screen.fill(background_color)
    screen.blit(rotated_animal_mouse, cursor_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
