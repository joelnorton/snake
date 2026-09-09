import random
import sys

import pygame

from constants import *
from player import *
from target import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    collidable = pygame.sprite.Group()

    Player.containers = (updatable, drawable, collidable)
    Target.containers = (drawable, updatable)

    random_x = random.randrange(RADIUS * 2, SCREEN_WIDTH - RADIUS * 2, RADIUS * 2)
    random_y = random.randrange(RADIUS * 2, SCREEN_HEIGHT - RADIUS * 2, RADIUS * 2)
    target = Target(
        random_x,
        random_y,
        RADIUS,
    )

    player = Player(100, 100, RADIUS)
    clock = pygame.time.Clock()

    while True:
        dt = clock.tick(60) / 1000
        screen.fill("black")
        updatable.update(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        if player.collide_wall(SCREEN_WIDTH, SCREEN_HEIGHT):
            print("Game Over")
            pygame.quit()
            return
        if player.collides_with(target):
            print(target.position)
            print(player.position)
            player.eat()
            target.kill()
            random_x = random.randrange(
                RADIUS * 2, SCREEN_WIDTH - RADIUS * 2, RADIUS * 2
            )
            random_y = random.randrange(
                RADIUS * 2, SCREEN_HEIGHT - RADIUS * 2, RADIUS * 2
            )
            target = Target(
                random_x,
                random_y,
                RADIUS,
            )
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
