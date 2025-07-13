# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    game_clock = pygame.time.Clock()
    
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
 
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0,0,0))
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

        time_passed = game_clock.tick(60)
        dt = time_passed / 1000

if __name__ == "__main__":
    main()