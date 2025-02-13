import pygame
from constants import *
from player import *
from circleshape import *

def main():
    pygame.init() # инициализация игры
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Подготовка холста + его размеры
    clock = pygame.time.Clock() # ...
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Создание игрока и постановка его в центр
    dt = 0 # смена кадра

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt) # обновление состояние игрока

        # Рендеринг (процесс в 3 этапа)
        screen.fill(BLACK) # красим экран в чёрный (постоянно)
        player.draw(screen) # рисуем игрока на экран
        pygame.display.flip() # показываем всё что нарисовали

        dt = clock.tick(60) / 1000 # ограничение в 60 кадров в секунду

if __name__ == "__main__":
    main()