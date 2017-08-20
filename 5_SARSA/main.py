from Environment import Environment
from Agent import Agent
from GraphicUtility import GraphicUtility
import pygame as pg
import os

if __name__ == "__main__":
    env = Environment()
    agent = Agent(env)
    graphic = GraphicUtility('SARSA', env)

    TARGET_FPS = 10
    clock = pg.time.Clock()

    for episode in range(1000):
        # 초반 행동 상태
        state = env.reset()
        action = agent.get_action(state)

        # 한 에피소드가 끝났는지
        done = False
        while not done:
            graphic.render(agent, env)

            # 행동을 환경에 전달 및 관찰(Observation)
            next_state, reward, done = env.step(action)

            # 다음 상태에서의 행동 선택
            next_action = agent.get_action(next_state)

            # [S, A, R, S', A']를 통해 업데이트
            agent.learn(state, action, reward, next_state, next_action)

            # 다음 상태로 변경
            state = next_state
            action = next_action

            # Event가 있는지(종료 키 누름 등) 확인
            graphic.check_event()

            # FPS
            clock.tick(TARGET_FPS)


        # 도착했을 시 모습을 그리고 좀 기다려주기
        graphic.render(agent, env)
        clock.tick(TARGET_FPS//3)




