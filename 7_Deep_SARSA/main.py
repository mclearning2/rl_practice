from GraphicUtility import GraphicUtility
from Environment import Environment
import pygame as pg

if __name__ == "__main__":
    env = Environment()
    graphic = GraphicUtility("Deep SARSA", env)

    TARGET_FPS = 10
    clock = pg.time.Clock()

    for episode in range(1000):

        done = False
        while not done:
            graphic.render(env)

            graphic.check_event()