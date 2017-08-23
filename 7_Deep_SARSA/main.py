from GraphicUtility import GraphicUtility
from Environment import Environment
import pygame as pg
import tensorflow as tf
import numpy as np

flags = tf.app.flags

flags.n_input = 10
flags.n_hidden1 = 30
flags.n_hidden2 = 30
flags.n_output = 4

def weight_variable(shape):
    return tf.Variable(tf.truncated_normal(shape, stddev=0.01))

def bias_variable(shape):
    return tf.Variable(tf.truncated_normal(shape))

def inference(input):

    x = tf.placeholder(dtype="float", shape=[None, flags.n_input])

    weights = {
        'h1': tf.Variable(tf.truncated_normal([flags.n_input, flags.n_hidden1])),
        'h2': tf.Variable(tf.truncated_normal([flags.n_hidden1, flags.n_hidden2])),
        'o': tf.Variable(tf.truncated_normal([flags.n_hidden2, flags.n_output]))
    }
    biases = {
        'h1': tf.Variable(tf.truncated_normal([flags.n_hidden1])),
        'h2': tf.Variable(tf.truncated_normal([flags.n_hidden2])),
        'o': tf.Variable(tf.truncated_normal([flags.n_output]))
    }

    h_layer1 = tf.add(tf.matmul(x, weights['h1']), biases['h1'])
    h_layer1 = tf.nn.relu(h_layer1)

    h_layer2 = tf.add(tf.matmul(h_layer1, weights['h2']), biases['h2'])
    h_layer2 = tf.nn.relu(h_layer2)

    output   = tf.matmul(h_layer2, weights['o']) + biases['o']
    return output

def get_action(state):
    pass

def train_model():
    pass

if __name__ == "__main__":
    env = Environment()
    graphic = GraphicUtility("Deep SARSA", env)

    FPS = 10
    clock = pg.time.Clock()

    for episode in range(1000):
        state = env.reset()
        state = np.reshape(state, [1, flags.n_input])
        print(state)

        done = False
        while not done:
            # 그리기
            graphic.render(env)

            # 장애물 움직이기
            env.move_obstacle()



            # 키누름이나 종료 확인
            graphic.check_event()

            # delay
            clock.tick(FPS)