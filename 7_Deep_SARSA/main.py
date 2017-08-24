from GraphicUtility import GraphicUtility
from Environment import Environment
from Agent import Agent
import pygame as pg

if __name__ == "__main__":
    env = Environment()
    agent = Agent(env)
    graphic = GraphicUtility("Deep SARSA", env)

    FPS = 10
    clock = pg.time.Clock()
    graphic_on = False
    for episode in range(100000):
        state = env.reset()

        score = 0

        done = False
        while not done:


            # 키누름이나 종료 확인(그리는 지 결정)
            graphic_on = graphic.check_event(graphic_on)

            # 그리기
            if graphic_on:
                clock.tick(FPS)
                graphic.render(env)

            # 장애물 움직이기
            env.move_obstacle()

            # 상태에 대한 행동
            action = agent.get_action(state)

            # 행동에 대한 결과 얻기
            next_state, reward, done = env.step(action)

            agent.train_model(state, action, reward, next_state, done)

            state = next_state

            score += reward

        if graphic_on:
            clock.tick(FPS//3)
            graphic.render(env)


        print('episode ', episode, ', score = ', score, ', epsilon = ', agent.epsilon)