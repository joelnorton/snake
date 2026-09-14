import random

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
    tails = []

    Player.containers = (updatable, drawable, collidable)
    Target.containers = (drawable, updatable)

    random_x = random.randrange(RADIUS * 2, SCREEN_WIDTH - RADIUS * 2, RADIUS * 2)
    random_y = random.randrange(RADIUS * 2, SCREEN_HEIGHT - RADIUS * 2, RADIUS * 2)
    target = Target(
        150,
        100,
        RADIUS,
    )

    player = Player(100, 100, RADIUS)
    clock = pygame.time.Clock()
    maxtails = 0

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
            player.eat()
            maxtails += RADIUS

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
        tails.append(player.position.copy())
        for i, tail in enumerate(tails):
            if i < len(tails) - maxtails:
                pygame.draw.circle(screen, "black", tail, RADIUS, 0)
            else:
                pygame.draw.circle(screen, "white", tail, RADIUS, 0)
                if player.collide_self(tail):
                    print("Game Over")
                    pygame.quit()
                    return

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
