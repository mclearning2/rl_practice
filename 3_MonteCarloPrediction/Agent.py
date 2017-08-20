import numpy as np
import random

class Agent:
    def __init__(self, env):
        self.learning_rate = 0.1   # 학습률
        self.discount_factor = 0.9 # 감가율
        self.epsilon = 0.2         # 탐욕
        self.samples = []          # 한 에피소드 발자취 저장

        # Q 함수
        self.value_table = [[0.0, 0.0, 0.0, 0.0] * env.grid_size \
                            for _ in range(env.grid_size)]

        # 환경 정보
        self.grid_size = env.grid_size
        self.possible_actions = env.possible_actions

    def update(self):
        G = 0                 # 반환값

        visited_state = []    # 왔던 길은 반영하지 않는다.

        for state, reward in reversed(self.samples):
            x, y = state

            if state not in visited_state:
                visited_state.append(state)

                G = reward + (self.discount_factor * G)
                self.value_table[y][x] += self.learning_rate * (G - self.value_table[y][x])



    def get_action(self, state):
        if np.random.rand() < self.epsilon:
            # 랜덤 행동
            return np.random.choice(self.possible_actions)
        else:
            max = -9999
            action_list = []

            # 가치함수에 따른 행동
            for action in self.possible_actions:
                x, y = state
                if action == 'UP':      y -= 1
                elif action == 'DOWN':  y += 1
                elif action == 'LEFT':  x -= 1
                elif action == 'RIGHT': x += 1

                # 범위 체크
                if not (y < 0 or y >= self.grid_size or \
                        x < 0 or x >= self.grid_size):
                    if max < self.value_table[y][x]:
                        action_list.clear()
                        action_list.append(action)
                        max = self.value_table[y][x]

                    elif max == self.value_table[y][x]:
                        action_list.append(action)


            return random.choice(action_list)




