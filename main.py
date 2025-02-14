import pygame
import sys 
from constants import *
from player import *
from circleshape import *
from asteroids import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt) 
        
        for obj in asteroids:
            if obj.check_colliding(player):
                print("GAME OVER")
                sys.exit()
            
        screen.fill(BLACK) 

        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            for shoot in shots:
                if shoot.check_colliding(asteroid):
                    asteroid.kill()
                    shoot.kill()
                    asteroid.split()

        pygame.display.flip() 

        dt = clock.tick(60) / 1000 

if __name__ == "__main__":
    main()