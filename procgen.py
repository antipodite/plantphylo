#! /usr/bin/env python
"""
Very simple procgen plant sim
June 2025
"""
import pygame
import random
import math
from collections import defaultdict

# Grid and window settings
WIDTH, HEIGHT = 600, 600
GRID_SPACING = 50
LINE_COLOR = (0, 0, 0)  # Black
WHITE = (255, 255, 255)  # White


#
# Logic
#

def get_neighbours(x, y, distance=1, grid_width=None, grid_height=None, include_center=False):
    """"Cherbyshev distance"""
    neighbors = []

    for dx in range(-distance, distance + 1):
        for dy in range(-distance, distance + 1):
            nx, ny = x + dx, y + dy
            steps = max(abs(dx), abs(dy))
            # Skip the center if not included
            if not include_center and dx == 0 and dy == 0:
                continue

            if grid_width is not None and (nx < 0 or nx >= grid_width):
                continue
            if grid_height is not None and (ny < 0 or ny >= grid_height):
                continue

            neighbors.append((int(nx), int(ny), steps))

    return neighbors


def raycast(start, direction, max_distance):
    x, y = start
    dx, dy = direction

    # Normalize direction
    length = math.hypot(dx, dy)
    dx /= length
    dy /= length

    cells = []

    # Initial grid cell
    gx, gy = int(x), int(y)

    step_x = 1 if dx > 0 else -1
    step_y = 1 if dy > 0 else -1

    t_max_x = ((gx + (dx > 0)) - x) / dx if dx != 0 else float('inf')
    t_max_y = ((gy + (dy > 0)) - y) / dy if dy != 0 else float('inf')

    t_delta_x = abs(1 / dx) if dx != 0 else float('inf')
    t_delta_y = abs(1 / dy) if dy != 0 else float('inf')

    for step in range(int(max_distance) + 1):  # +1 to include the last step
        cells.append((gx, gy, step))
        
        if t_max_x < t_max_y:
            t_max_x += t_delta_x
            gx += step_x
        else:
            t_max_y += t_delta_y
            gy += step_y

    return cells


def make_rect(grid_x, grid_y, grid_pixels):
    return (grid_x * grid_pixels, grid_y * grid_pixels, grid_pixels, grid_pixels)


class World:
    def __init__(self, size_x, size_y, light_sources):
        self.size_x = size_x
        self.size_y = size_y
        self.light_sources = light_sources
        self.cells = [[0 for x in range(size_x)] for y in range(size_y)]
        self.objects = []

    def render(self, screen, grid_pixels, show_sources = False):
        screen.fill(WHITE)
        
        for y in range(self.size_y):
            for x in range(self.size_x):
                cell_value = self.cells[y][x]
                light_colour = (255, 255, 255 - (cell_value * 20))
                rect = make_rect(x, y, grid_pixels)
                try:
                    print(f"Cell: ({x},{y}), value: {cell_value}, level: {light_colour}, rect: {rect}")                
                    pygame.draw.rect(screen, light_colour, rect)
                    
                    if show_sources:
                        for source_x, source_y in self.light_sources:
                            pygame.draw.rect(screen, (255, 0, 0), make_rect(source_x, source_y, grid_pixels), width = 2)
                except Exception as e:
                    raise e

    def illuminate(self):
        for x, y in self.light_sources:
            nn = get_neighbours(x, y,
                                distance = max(self.size_x, self.size_y),
                                grid_width = self.size_x,
                                grid_height = self.size_y)
            for x, y, dist in nn:
                self.cells[y][x] = dist

    def raycast_illuminate(self):
        # For now just cast a ray straight down from a row of lights at top
        for source in self.light_sources:
            for x, y, step in raycast(source, (0, 1), self.size_y - 1):
                self.cells[y][x] = step
        


#
# Display
#

def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Pygame 2D Grid")

    world = World(10, 10, light_sources = [(x, 0) for x in range(10)])
    world.raycast_illuminate()
    # Main loop
    running = True
    while running:


        world.render(screen, grid_pixels = 100, show_sources = True)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    main()
