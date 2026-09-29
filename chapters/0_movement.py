import pygame
from helpers import draw_arrow


WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
MAX_FPS = 60


pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.Clock()
is_running = True


# A vector in linear algebra is ordered finite list of numbers. There are several
# perspectives to approach and understand vectors.
#
# However, in computer graphics and games, they are mostly used as coordinates in
# space. For example an NPC's position, a spaceship's velocity, etc.
#
# In a 500x500 pixel screen, if you want a character placed in the middle, you
# would place it at (250, 250). Since our screen is a 2D space of pixels, our
# vector coordinate is also 2D.
#
# Now instead of hardcoding the numbers, let's use the resolution variables to
# put a coordinate at the middle, named "position":
position = pygame.Vector2(WINDOW_WIDTH / 2.0, WINDOW_HEIGHT / 2.0)

# That's cool and all, but why bother using pygame.Vector2 when, let's say, we
# could have just used a tuple? Or X and Y variables?
#
# Because a vector is not simply a data structure to hold two numbers. It has
# way more functionality.
#
# In a physics view, vector is an arrow in space possessing a specific magnitude
# (length) and direction. There are specific methods, such as pygame.Vector2.rotate
# or pygame.Vector2.mangnitude that gives you exactly those properties.
#
# You can also apply linear algebra. Let's say we have a vector that is exactly
# 5 pixels long, but rotated 45 degrees:
#
# v = pygame.Vector2(5.0, 0.0).rotate(45)
#
# If you printed the components of the vector, you would see random numbers (because
# it was rotated). But it's still 5 units long. We can multiply the vtor just by
# a scalar:
#
# v_longer = v * 3.0
#
# And now our vector is 15 units long, but still rotated 45 degrees.

# Our position vector represents a position in screen as pixels. However, one
# does not necessarily need to have an origin.
velocity = pygame.Vector2()

# We created a velocity vector, since no parameters, it's a zero vector. However,
# this doesn't mean it's on the top-left side of the screen or whatever.
#
# The velocity vector is not on screen space. It's bound to our position. You can
# think of it as glued to our position vector, following it wherever it goes. This
# can be achieved with a simple addition:
#
# new_position = position + velocity
#
# When you add two vectors together, you basically get the displacement of our
# position vector.


while is_running:
    clock.tick(MAX_FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

    keys = pygame.key.get_pressed()

    # Construct the velocity vector every frame from the pressed keys
    # so it's not persistent across frames, it just represents what keys are pressed
    velocity = pygame.Vector2(0, 0)
    if keys[pygame.K_a]: velocity.x = -5
    if keys[pygame.K_d]: velocity.x = 5
    if keys[pygame.K_w]: velocity.y = -5
    if keys[pygame.K_s]: velocity.y = 5

    # Current position displacement
    displacement = position + velocity

    # Replace the previour position by placement to move around space
    position = displacement

    screen.fill((255, 255, 255))

    draw_arrow(screen, "lime", pygame.Vector2(), position)

    # Notice how I multiple velocity by a scalar to make the arrow longer
    draw_arrow(screen, "magenta", position, displacement + velocity * 10)

    pygame.display.flip()
    pygame.display.set_caption(f"Pygame Physics Tutorial - Chapter 0: Movement - {round(clock.get_fps())} FPS")

pygame.quit()