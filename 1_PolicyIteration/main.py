from Agent import Agent
from Environment import Environment
from GraphicUtility import GraphicUtility

if __name__ == "__main__":
    print('Key Information')
    print('----------------------------------')
    print('e | policy evaluation')
    print('i | policy improvement')
    print('m | move')
    print('r | reset')
    print('----------------------------------')

    env = Environment()
    agent = Agent(env)
    util = GraphicUtility('Policy Iteration', agent)
    util.main_loop()
