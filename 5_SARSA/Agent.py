import numpy as np
import random

class Agent:
    def __init__(self, env):
        self.learning_rate = 0.1   # 학습률
        self.discount_factor = 0.9 # 감가율
        self.epsilon = 0.2         # 탐욕
        self.samples = []          # 한 에피소드 발자취 저장

        # 큐함수
        self.Q_table = np.zeros([5,5,4],dtype=np.float32)

        # 환경 정보
        self.grid_size = env.grid_size
        self.possible_actions = env.possible_actions

    def learn(self, state, action, reward, next_state, next_action):

         cur_x, cur_y = state
         cur_act_index = self.possible_actions.index(action)

         next_x, next_y = next_state
         next_act_index = self.possible_actions.index(next_action)

         cur_state_q = self.Q_table[cur_y][cur_x][cur_act_index]
         next_state_q = self.Q_table[next_y][next_x][next_act_index]

         self.Q_table[cur_y][cur_x][cur_act_index] += self.learning_rate * (reward +
                                 self.discount_factor * next_state_q - cur_state_q)


    def get_action(self, state):
        # 탐험 : 랜덤 행동
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.possible_actions)
        else:
            max = -9999
            x, y = state
            action_list = []

            # 큐함수에 따른 행동
            for index, value in enumerate(self.Q_table[y][x]):
                action = self.possible_actions[index]

                if max < value:
                    action_list.clear()
                    action_list.append(action)
                    max = value

                elif max == value:
                    action_list.append(action)


            return random.choice(action_list)
