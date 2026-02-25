import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Skull Animation")

clock = pygame.time.Clock()

x = WIDTH // 2
y = HEIGHT // 2
speed_x = 6
speed_y = 5

angle = 0
trail = []


def draw_skull(surface, x, y, size, color, angle):
    skull_surface = pygame.Surface((size*2, size*2), pygame.SRCALPHA)

    # Head
    pygame.draw.circle(skull_surface, color, (size, size), size)

    # Eyes
    pygame.draw.circle(skull_surface, (0, 0, 0),
                       (size - size//3, size - size//4), size//6)
    pygame.draw.circle(skull_surface, (0, 0, 0),
                       (size + size//3, size - size//4), size//6)

    # Nose
    pygame.draw.polygon(skull_surface, (0, 0, 0), [
        (size, size),
        (size - size//8, size + size//5),
        (size + size//8, size + size//5)
    ])

    # Teeth
    pygame.draw.rect(skull_surface, (0, 0, 0), (size - size //
                     2, size + size//3, size, size//3), 2)

    # Rotate skull
    rotated = pygame.transform.rotate(skull_surface, angle)
    rect = rotated.get_rect(center=(x, y))
    surface.blit(rotated, rect)


running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    x += speed_x
    y += speed_y

    if x <= 60 or x >= WIDTH-60:
        speed_x *= -1
    if y <= 60 or y >= HEIGHT-60:
        speed_y *= -1

    # Change color slowly
    r = int((math.sin(pygame.time.get_ticks() * 0.002) + 1) * 127)
    g = int((math.sin(pygame.time.get_ticks() * 0.003) + 1) * 127)
    b = int((math.sin(pygame.time.get_ticks() * 0.004) + 1) * 127)
    color = (r, g, b)

    angle += 2

    # Trail effect
    trail.append((x, y))
    if len(trail) > 15:
        trail.pop(0)

    screen.fill((10, 10, 20))

    for i, pos in enumerate(trail):
        alpha = int(255 * (i / len(trail)))
        trail_surface = pygame.Surface((120, 120), pygame.SRCALPHA)
        draw_skull(trail_surface, 60, 60, 40, (*color, alpha), angle)
        screen.blit(trail_surface, (pos[0]-60, pos[1]-60))

    draw_skull(screen, x, y, 60, color, angle)

    pygame.display.flip()

pygame.quit()
