import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # delta time in seconds
    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if asteroid.checkCollisionWith(player):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if asteroid.checkCollisionWith(bullet):
                    bullet.kill()
                    asteroid.split()
                    break

        # create screen
        screen.fill("black")

        # render game
        for item in drawable:
            item.draw(screen)

        # flip the display to put created scene on screen
        pygame.display.flip()

        dt_ms = clock.tick(60)  # limit to 60 FPS, delta time in milliseconds
        dt = (
            dt_ms / 1000
        )  # amount of time since tick() was called last time, in seconds

    pygame.quit()


if __name__ == "__main__":
    main()
