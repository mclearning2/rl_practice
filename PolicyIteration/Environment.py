import pygame as pg

DISCOUNT_FACTOR = 0.9

class Environment():
    def __init__(self):
        self.grid_x     = 5
        self.grid_y     = 5
        self.grid_pixel = 100

        self.reward = [ [0.0] * self.grid_x for _ in range(self.grid_y) ]

        self.transition_probability = 1

    def draw(self):
        pass

    def step(self, state, action):
        x, y = state
        if action == 'UP' and y >= 0:
            y -= 1
        if action == 'DOWN' and y < self.grid_y:
            y += 1
        if action == 'LEFT' and x >= 0:
            x -= 1
        if action == 'RIGHT' and x < self.grid_x:




    def get_reward(self, state, action):
        x, y = self.step(state, action)
        return self.reward[x][y]

if __name__ == '__main__':
    env = Environment()
