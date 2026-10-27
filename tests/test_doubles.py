
import pygame
import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))

from ship import Ship
from settings import Settings
from tests.doubles import StubShipSettings


def test_ship_move_right_with_stub():
    pygame.init()
    pygame.display.set_mode((800, 600))

    try:
        screen = pygame.display.get_surface()
        settings = Settings()
        settings.ship_speed = 10

        # O stub fornece a velocidade controlada para a nave.
        stub_settings = StubShipSettings(ship_speed=10)
        ship = Ship(screen, stub_settings)

        x_inicial = ship.x
        ship.moving_right = True
        ship.update()

        assert ship.x == x_inicial + 10
    finally:
        pygame.quit()



def test_ship_blit_calls_screen_blit(mocker):
    pygame.init()

    try:
        # Cria um mock para representar a tela.
        screen_mock = mocker.Mock()
        screen_mock.get_rect.return_value = pygame.Rect(0, 0, 800, 600)

        settings = Settings()
        ship = Ship(screen_mock, settings)

        ship.blitme()

        screen_mock.blit.assert_called_once_with(
            ship.image,
            ship.rect,
        )
    finally:
        pygame.quit()
