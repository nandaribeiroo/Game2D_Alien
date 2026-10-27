
import pygame
import sys
from pathlib import Path

# Adiciona a pasta src ao caminho de busca do Python
SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))

from ship import Ship
from settings import Settings


def test_ship_move_right():
    pygame.init()
    pygame.display.set_mode((800, 600))

    screen = pygame.display.get_surface()
    settings = Settings()
    ship = Ship(screen, settings)

    x_inicial = ship.x

    ship.moving_right = True
    ship.update()

    assert ship.x > x_inicial

    pygame.quit()
