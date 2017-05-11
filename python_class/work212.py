import random, csv
from copy import copy, deepcopy
# deepcopy : 메모리를 완전히 새롭게 생성
# copy : 껍데기만 카피, 내용은 동일한 곳을 가리킴
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
DRAW = 3

BOARD_FORMAT = "\n\
┌───────────────────────────────────┐\n\
| {0} | {1} | {2} | {3} |\n\
|-----------------------------------|\n\
| {4} | {5} | {6} | {7} |\n\
|-----------------------------------|\n\
| {8} | {9} | {10} | {11} |\n\
|-----------------------------------|\n\
| {12} | {13} | {14} | {15} |\n\
└───────────────────────────────────┘"

NAMES = [' ', 'X', 'O']

# 보드 출력
def printboard(state):
    cells = []
    for i in range(4):
        for j in range(4):
            cells.append(NAMES[state[i][j]].center(6)) # center(6) 은 뭘까???
    print(BOARD_FORMAT.format(*cells))


# 빈 판
def emptystate():
    return [[EMPTY, EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY, EMPTY]]

def gameover(state):
    # 가로/세로로 한 줄 완성한 플레이어가 있다면 그 플레이어 리턴
    for i in range(4):
        if state[i][0] != EMPTY and state[i][0] == state[i][1] and state[i][0] == state[i][2] and state[i][0] == state[i][3]:
            return state[i][0]
        if state[0][i] != EMPTY and state[0][i] == state[1][i] and state[0][i] == state[2][i] and state[0][i] == state[3][i]:
            return state[0][i]
    # 좌우 대각선
    if state[0][0] != EMPTY and state[0][0] == state[1][1] and state[0][0] == state[2][2] and state[0][0] == state[3][3]:
        return state[0][0]
    if state[0][3] != EMPTY and state[0][3] == state[1][2] and state[0][3] == state[2][1] and state[0][3] == state[3][0]:
        return state[0][3]
    # 판이 비었는지
    for i in range(4):
        for j in range(4):
            if state[i][j] == EMPTY:
                return EMPTY
    return DRAW
# 사람
class Human(object):
    def __init__(self, player):
        self.player = player

    # 착수
    def action(self, state):
        printboard(state)
        action = None
        while action not in range(1, 17):
            action = int(input('Your move? '))
        switch_map = {
            1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (0, 3),
            5: (1, 0),
            6: (1, 1),
            7: (1, 2),
            8: (1, 3),
            9: (2, 0),
            10: (2, 1),
            11: (2, 2),
            12: (2, 3),
            13: (3, 0),
            14: (3, 1),
            15: (3, 2),
            16: (3, 3)
        }
        return switch_map[action]

    def episode_over(self, winner):
        if winner == DRAW:
            print('Game over! It was a draw.')
        else:
            print('Game over! Winner: Player {0}'.format(winner))


def play(agent1, agent2):
    state = emptystate()
    for i in range(9):
        if i % 2 == 0:
            move = agent1.action(state)
        else:
            move = agent2.action(state)
        state[move[0]][move[1]] = (i % 2) + 1
        winner = gameover(state)
        if winner != EMPTY:
            return winner
    return winner

class Computer(object):
    def __init__(self, player):
        self.player = player
        self.values = {} # csv 에 있는 파일의 내용(9개의 판(수)과 가중치)를 읽어서 저장할 딕셔너리 변수
        self.readCSV() # init 할때 values 에 값 채워넣을려고 함수를 실행함
        self.verbose = True
        #print(self.values) # {((0, 2, 1), (2, 2, 0), (1, 1, 0)): -0.999999,...
                           #  위와 같이 values 딕셔너리 변수에 저장되어 있는지 확인한다.

    def readCSV(self):
        file = open("C:\\data\\test100000.csv", 'r')
        ttt_list = csv.reader(file)
        for t in ttt_list:
            try:
                self.values[((int(t[0]) ,int(t[1]) ,int(t[2])),(int(t[3]) ,int(t[4]) ,int(t[5])) ,(int(t[6]) ,int(t[7])
                             ,int(t[8])))] = float(t[10])
            except ValueError:    # {((0, 2, 1), (2, 2, 0), (1, 1, 0)): -0.999999,..
                continue

    def random(self, state):  # 남아있는 비어 있는 수들 중에서 한수를 random 으로 고르기 위한 함수
        available = []
        for i in range(4):
            for j in range(4):
                if state[i][j] == EMPTY:
                    available.append((i ,j))
        return random.choice(available)

    def greedy(self, state):
        maxval = -50000  # 남아있는 수중에 가장 좋은 수의 가중치를 담기 위해  선언
        maxmove = None   # 남아있는 수중에 가장 좋은 수를 담기 위해 선언
        if self.verbose:  # 수를 둘때마다 남아있는 수들의 확률을 확인하기 위해서 사용하는 코드
            cells = []
        for i in range(4):
            for j in range(4):
                if state[i][j] == EMPTY: # 남아있는 수중에 비어있는 수를 찾아서
                    state[i][j] = self.player # 거기에 플레이어의 숫자를 넣은후
                    val = self.lookup(state) # values 에 없으면 새로 0.5 를
                    #print(val)               # values 에 넣어주고 그 값을 다시 여기로 가져온다
                                              # 있으면 바로 values 에서 가져온다. (-0.9606 )
                    state[i][j] = EMPTY      # 그 수를 다시 비워준다.

                    if val > maxval:
                        maxval = val
                        # print (maxval) # 남아있는 수중에 가장 큰게 0.029698 (0.030) 이었음
                        maxmove = (i, j)
                        #print(maxmove)   # 남아있는 수중에 가장 가장치가 큰 자리 (2,0)
                    if self.verbose:  #
                        cells.append('{0:.3f}'.format(val).center(6))
                elif self.verbose:
                    cells.append(NAMES[state[i][j]].center(6))
        if self.verbose:
            print (BOARD_FORMAT.format(*cells))

        return maxmove

    def lookup(self, state):
        key = self.statetuple(state) # 리스트를 튜플로 바꿔주는 역활
        if not key in self.values: # 위의  key 수들이 csv 에서 읽어온 수들중에 없다면
            self.add(key)  # values 에 없으며 add 함수로 추가
        return self.values[key]  # 있으면 그거 리턴, 없으면 만들고 리턴

    def add(self, state):
        winner = gameover(state)
        tup = self.statetuple(state)
        self.values[tup] = self.winnerval(winner) # 1,-1,0.5, 0 (비긴것)

    def statetuple(self, state):
        return (tuple(state[0]) ,tuple(state[1]) ,tuple(state[2]), tuple(state[3]))

    # 컴퓨터가 착수
    def action(self, state):
        printboard(state)
        action = None
        move = self.greedy(state)
        state[move[0]][move[1]] = self.player
        return move

    def winnerval(self, winner):
        if winner == self.player:
            return 1
        elif winner == EMPTY:
            return 0.5
        elif winner == DRAW:
            return 0
        else:
            return self.lossval

    def episode_over(self, winner):
        if winner == DRAW:
            print('Game over! It was a draw.')
        else:
            print('Game over! Winner: Player {0}'.format(winner))


if __name__ == "__main__":
    p1 = Agent(1, lossval=-1)
    p2 = Agent(2, lossval=-1)

    for i in range(10000):
        if i % 10 == 0:
            print('Game: {0}'.format(i))

        winner = play(p1, p2)
        p1.episode_over(winner)
        p2.episode_over(winner)

    while True:
        p2.verbose = True
        p1 = Human(1)
        winner = play(p1, p2)
        p1.episode_over(winner)
        p2.episode_over(winner)

