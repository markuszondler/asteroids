import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    print("Starting asteroids!")
    pygame.init()

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # delta time in seconds
    running = True

    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # create screen
        screen.fill("black")

        # render game

        # flip the display to put created scene on screen
        pygame.display.flip()

        dt_ms = clock.tick(60)  # limit to 60 FPS, delta time in milliseconds
        dt = (
            dt_ms / 1000
        )  # amount of time since tick() was called last time, in seconds

    pygame.quit()


if __name__ == "__main__":
    main()
