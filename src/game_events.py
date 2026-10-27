
import sys

import pygame

from bullet_manager import BulletManager
from ship import Ship


class GameEventHandler:
    """Responsável por ler e tratar eventos do teclado e da janela."""

    def __init__(self, ship: Ship, bullet_manager: BulletManager) -> None:
        self.ship = ship
        self.bullet_manager = bullet_manager

    def _check_events(self) -> None:
        """Responde aos eventos de teclado e fechamento da janela."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event)
            elif event.type == pygame.KEYUP:
                self._handle_keyup(event)

    def _handle_keydown(self, event: pygame.event.Event) -> None:
        """Responde aos eventos de pressionamento de teclas."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.bullet_manager._fire_bullet()

    def _handle_keyup(self, event: pygame.event.Event) -> None:
        """Responde aos eventos de soltura de teclas."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False