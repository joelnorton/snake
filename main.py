import random
import sys

import pygame

from constants import *
from player import *
from tail import *
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
    Tail.containers = (drawable, collidable)

    random_x = random.randrange(RADIUS * 2, SCREEN_WIDTH - RADIUS * 2, RADIUS * 2)
    random_y = random.randrange(RADIUS * 2, SCREEN_HEIGHT - RADIUS * 2, RADIUS * 2)
    target = Target(
        150,
        100,
        RADIUS,
    )

    player = Player(100, 100, RADIUS)
    clock = pygame.time.Clock()

    while True:
        dt = clock.tick(60) / 1000
        screen.fill("black")
        oldplayer = player
        updatable.update(dt)
        newtail = False
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
            newtail = True
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

        # if (
        #     len(tails) > 0
        #     and player.change_at != tails[0].change_at
        #     and player.change_at != pygame.Vector2(0, 0)
        # ):
        #     tails[0].change_at = player.change_at
        #     tails[0].change_direction = player.direction
        #     tails[0].change_cardinal_direction = player.cardinal_direction
        #     # player.change_at = pygame.Vector2(0, 0)
        for i in range(len(tails), 0, -1):
            if i == 1:
                previous = oldplayer

            else:
                previous = tails[i - 2]

            if player.change_at != tails[
                0
            ].change_at and player.change_at != pygame.Vector2(0, 0):
                tails[i - 1].change_at = previous.change_at.copy()
                tails[i - 1].change_direction = previous.direction.copy()
                tails[i - 1].change_cardinal_direction = previous.cardinal_direction
                tails[i - 1].changed = False
                print(
                    f"Updating directions for {i}: {tails[i - 1].change_direction}, {tails[i - 1].change_cardinal_direction}, {tails[i - 1].change_at}"
                )

            if newtail == True and i == len(tails):
                current = tails[i - 1]
                tails.append(
                    Tail(
                        int(current.position.x),
                        int(current.position.y),
                        RADIUS,
                        current.cardinal_direction,
                        current.velocity,
                        current.speed,
                        current.change_at,
                        current.change_direction,
                        current.direction,
                    )
                )
            elif len(tails) > 0:
                tails[i - 1].update_tail(
                    previous.position,
                    previous.velocity,
                    previous.cardinal_direction,
                    player.steps,
                    previous.change_at,
                    previous.speed,
                )
                if previous.position.distance_to(tails[i - 1].position) > RADIUS * 4:
                    sys.exit()
            tails[i - 1].draw(screen)

        if len(tails) == 0 and newtail == True:
            tails.append(
                Tail(
                    int(oldplayer.position.x),
                    int(oldplayer.position.y),
                    RADIUS,
                    player.cardinal_direction,
                    player.velocity,
                    player.speed,
                    player.change_at,
                    player.direction,
                    player.direction,
                )
            )
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
