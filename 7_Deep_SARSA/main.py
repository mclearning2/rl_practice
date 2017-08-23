from GraphicUtility import GraphicUtility
from Environment import Environment
import pygame as pg

if __name__ == "__main__":
    env = Environment()
    graphic = GraphicUtility("Deep SARSA", env)

    FPS = 10
    clock = pg.time.Clock()

    for episode in range(1000):

        done = False
        while not done:
            # 그리기
            graphic.render(env)

            # 장애물 움직이기
            env.move_obstacle()


            graphic.check_event()

            clock.tick(FPS)