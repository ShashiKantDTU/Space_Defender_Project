import pygame
import sys

pygame.init()

# Load the image
image = pygame.image.load("menu.png")
image_rect = image.get_rect()

# Set initial alpha value
alpha_value = 255

# Create a clock object
clock = pygame.time.Clock()

# Create a window
screen = pygame.display.set_mode((800, 600))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Decrement alpha value every frame
    alpha_value -= 1
    if alpha_value < 0:
        alpha_value = 255

    # Set the image's alpha value
    image.set_alpha(alpha_value)

    # Draw the image onto the screen
    screen.fill((0, 0, 0))
    screen.blit(image, image_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 30 FPS
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
