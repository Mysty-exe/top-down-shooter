import pygame
import project.constants as constants
import project.events as events
from project.characters import Player
from project.math import Vector


class View:

    def __init__(self):
        self.width, self.height = constants.GAME_WIDTH, constants.GAME_HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))


class GameView(View):

    def __init__(self):
        View.__init__(self)
        self.player = Player()
        self.k_input = events.KeyboardInput()
        self.m_input = events.MouseInput()

    def run(self, dt, state):
        self.screen.fill(constants.COLOURS['white'])

        k_events = self.k_input.process_events(pygame.key.get_pressed())
        m_events = self.m_input.process_events(pygame.mouse.get_pressed()[0],
                                               pygame.mouse.get_pos())

        self.player.draw(self.screen)
        self.player.move(dt, k_events)
        self.player.reset_direction(k_events)
        self.k_input.empty_queue()
        mouseDirection = m_events - self.player.vector
        pygame.draw.line(
            self.screen, constants.COLOURS['white'], self.player.vector.coord(),
            (mouseDirection.normalize() * 25 + self.player.vector).coord())
        print(self.player.vector.dot(m_events))

        return state
