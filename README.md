# 강화학습 정리, 실습 코드

올 한해 가장 맘에 드는 이 책! 산 것을 절대 후회하지 않습니다! 강화학습에 발목 붙잡혀 공부하기 힘들어하던 제게 한줄기 빛같은 존재!! 감사합니다! 깊은 존경을 표합니다. 어찌되었건 완독과 완벽한 이해, 그리고 코드로 짜보겠다는 목표로 8월 말까지 해볼 생각입니다.

![| center](./book.png)

>**이 코드는 [파이썬과 케라스로 배우는 강화학습 책 코드](https://github.com/rlcode/reinforcement-learning-kr)를 기반으로 만들어 졌습니다.**

공부용으로 만들어진 것이며 기존의 책과는 다르게 짜여져있습니다. 제가 이해한 바를 토대로 새로 짰기 때문에 어느정도 다릅니다. 또한 tkinter 대신 pygame 기반으로 짜였기 때문에 Button 같은 GUI가 없습니다. 대신 key를 누르며 커맨드 창에 설명을 적었습니다.

이론은 [블로그](http://cineraria219.tistory.com/category/Study/%EA%B0%95%ED%99%94%ED%95%99%EC%8A%B5)에 약간 정리했습니다. 하지만 어디까지나 요약에 가깝기 때문에 설명이 상세하지 않으며 친절하게도 설명되어 있지 않기 때문에 책을 보시는 것을 추천합니다.(책 짱짱맨)

## 필요한 환경
1. python 3.5
2. numpy 1.13.1
3. pygame 1.9.3

# 실행 방법
우선 git clone을 통해 코드를 받아주시구

``` bash
git clone https://github.com/KiMC2/Reinforcement_Example.git
```

코드를 실행하기 위해 패키지 설치를 설치합니다.
``` bash
pip install -r requirements.txt
```

각 폴더에는 main.py가 있습니다. 어떤 툴을 쓰거나 커맨드창에서 실행해주시면 됩니다.
``` bash
python main.py
```

## 목차 (Table of Contents)
1. [정책 이터레이션(Policy Iteration)](https://github.com/KiMC2/Reinforcement_Example/tree/master/PolicyIteration)
2. [가치 이터레이션(Value Iteration)](https://github.com/KiMC2/Reinforcement_Example/tree/master/2_ValueIteration)
3. [몬테 카를로 예측(Monte Carlo Prediction)](https://github.com/KiMC2/Reinforcement_Example/tree/master/3_MonteCarloPrediction)
4. [시간차 예측(Temporal Diffrenece Learning)](https://github.com/KiMC2/Reinforcement_Example/tree/master/4_TemporalDifferenceLearning)
5. [살사(SARSA)](https://github.com/mclearning2/rl_practice/tree/master/5_SARSA)
6. [큐러닝(Q-Learning)](https://github.com/mclearning2/rl_practice/tree/master/6_Q-Learning)
7. [딥살사(Deep_SARSA)](https://github.com/mclearning2/rl_practice/tree/master/7_Deep_SARSA)
8. [DQN](https://github.com/mclearning2/rl_practice/tree/master/8_DQN)