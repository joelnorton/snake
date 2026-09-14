import pygame

from constants import *
from shape import Shape


class Tail(Shape):
    def __init__(
        self,
        x: int,
        y: int,
        radius: int,
        cardinal_direction: int,
        velocity: pygame.Vector2,
        speed: int,
        change_at: pygame.Vector2,
        change_direction: pygame.Vector2,
        direction: pygame.Vector2,
    ) -> None:
        match cardinal_direction:
            case 0:
                x = x - radius * 2
            case 1:
                y = y - radius * 2
            case 2:
                x = x + radius * 2
            case 3:
                y = y + radius * 2
        super().__init__(x, y, radius)
        self.cardinal_direction = cardinal_direction
        self.velocity = velocity
        self.change_at = change_at
        self.change_direction = change_direction
        self.change_cardinal_direction = cardinal_direction
        self.speed = speed
        self.direction = direction
        self.changed = False

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, 0)

    def update_tail(
        self,
        position: pygame.Vector2,
        velocity: pygame.Vector2,
        cardinal_direction: int,
        steps: int,
        change_at: pygame.Vector2,
        player_speed: int,
    ) -> None:
        if (
            self.position.distance_to(self.change_at) < self.radius
            and steps >= 20 / player_speed
            and not self.changed
        ):
            self.position = self.change_at.copy()
            self.velocity = self.change_direction.copy() * player_speed
            # self.change_at = pygame.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)
            self.cardinal_direction = self.change_cardinal_direction
            self.changed = True
        else:
            self.position += self.velocity.copy()
        self.change_at = change_at
        self.change_cardinal_direction = cardinal_direction
