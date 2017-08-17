import random as pr
import numpy as np

class Agent():
    def __init__(self, env):
        # 환경
        self.env = env

        # 가치함수 테이블
        self.value_func = [[0.0] * env.grid_size for _ in range(env.grid_size)]

        # 감가율
        self.discount_factor = 0.9

        # 움직임 스위치
        self.doMove = False

    def _get_value_func(self, state):
        x, y = state
        return self.value_func[y][x]

    def value_iteration(self):
        next_value_func = self.value_func

        for y in range(self.env.grid_size):
            for x in range(self.env.grid_size):
                # 행동 중 최대 가치함수를 저장
                max_value = -9999

                # 현재 상태
                state = (x, y)

                # 각 상태의 모든 행동에 대한 가치함수들을 비교한다.
                for action in self.env.possible_actions:
                    # 목표 지점에서는 가치함수를 따지지 않는다.
                    if state == self.env.goal_coord:
                        value = 0.0
                        break

                    # 벨만 방정식
                    else:
                        # 다음 상태
                        next_state = self.env.step(state, action)

                        # 다음 상태의 보상
                        reward = self.env.get_reward(next_state)

                        # 다음 상태의 가치함수
                        next_value = self._get_value_func(next_state)

                        # 가치 함수 = 정책 x (다음 상태의 보상 + 감가율 x 다음 상태 가치함수)
                        value = reward + self.discount_factor * next_value

                        if max_value < value:
                            max_value = value
                            next_value_func[y][x] = value

        self.value_func = next_value_func


    def move(self):
        x, y = self.env.unit_coord

        max_value = -9999
        max_value_list = []

        # 움직이기 시작골인 지점이면 가만히
        if not self.env.unit_coord == self.env.goal_coord:
            # 각 상태의 모든 행동에 대한 가치함수들을 비교한다.
            for action in self.env.possible_actions:

                next_state = self.env.step(self.env.unit_coord, action)

                reward = self.env.get_reward(next_state)

                next_value = self._get_value_func(next_state)

                value = reward + self.discount_factor * next_value

                if value == max_value:
                    max_value_list.append(value)
                elif value > max_value:
                    max_value_list.clear()
                    max_value_list.append(value)
                    max_value = value

                indices = np.nonzero(max_value_list == max_value)[0] # array([max_index_list], dtype=int64)
                action = pr.choice(indices)

                self.env.unit_coord = self.env.step(self.env.unit_coord, action)

    def reset(self):
        # 가치함수 테이블
        self.value_func = [[0.0] * self.env.grid_size for _ in range(self.env.grid_size)]

        # 환경 리셋
        self.env.reset()
