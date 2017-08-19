class Environment():
    def __init__(self, grid_size = 5, unit_coord=(0,0), goal_coord=(2,2), obstacle_coord= [[1, 2], [2, 1]]):
        # 그리드 크기
        self.grid_size  = grid_size

        # 유닛 초기 지점 좌표
        self.coord = {'unit': unit_coord,
                      'goal': goal_coord,
                      'obstacle': obstacle_coord}

        self.unit_start_point = unit_coord

        # 보상들
        self.reward_table = [ [0] * self.grid_size for _ in range(self.grid_size) ]
        self.reward_table[self.coord['goal'][0]][self.coord['goal'][1]] = 1

        for o_coord in self.coord['obstacle']:
            x, y = o_coord
            self.reward_table[y][x] = -1

        # 가능한 행동 모음( 상 하 좌 우 )
        self.possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']

    def _is_boundary_out(self, x, y):
        return x < 0 or x >= self.grid_size or \
               y < 0 or y >= self.grid_size

    def _reward_check(self, state):
        reward = 0
        done = False
        for x, y in self.coord['obstacle']:
            if state == (x, y):
                reward = -1
                done = True
        if state == self.coord['goal']:
            reward = 1
            done = True

        return reward, done

    def step(self, action):

        x, y = self.coord['unit']
        next_state = (x, y)

        if action == 'UP': y -= 1
        elif action == 'DOWN': y += 1
        elif action == 'LEFT': x -= 1
        elif action == 'RIGHT': x += 1

        if not self._is_boundary_out(x, y):
            next_state = x, y

        self.coord['unit'] = next_state

        reward, done = self._reward_check((x, y))

        return next_state, reward, done

    def reset(self):
        # 보상들
        self.reward_table = [[0] * self.grid_size for _ in range(self.grid_size)]
        self.reward_table[self.coord['goal'][0]][self.coord['goal'][1]] = 1

        for o_coord in self.coord['obstacle']:
            x, y = o_coord
            self.reward_table[y][x] = -1

        self.coord['unit'] = self.unit_start_point

        return self.unit_start_point



