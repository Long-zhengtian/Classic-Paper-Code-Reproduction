import random
import copy
import string

import numpy
import tqdm
import networkx
import networkt
# import taichi as ti
# import taichi.math as tm
from numba import jit, njit
from player import players, playersInit
from config import *
from output import output2File
from alive_progress import alive_bar


def play(x: int, y: int, _PayOff):  # 双方进行博弈，返回收益  x,y为index
    if players[x].strategy and players[y].strategy:  # 都合作
        return _PayOff.R
    elif players[x].strategy and not players[y].strategy:
        return _PayOff.S
    elif not players[x].strategy and players[y].strategy:
        return _PayOff.T
    else:  # 都对抗
        return _PayOff.P


def strategyUpdate(x, y, _PayOff, Game, NOCs):  # 策略的更新过程
    if players[y].AccPayOffs > players[x].AccPayOffs:
        D = _PayOff.T - _PayOff.S if Game == "PD" else _PayOff.T - _PayOff.P
        k_max = max(np.count_nonzero(NOCs[x]), np.count_nonzero(NOCs[y]))
        UpdateProbability = (players[y].AccPayOffs - players[x].AccPayOffs) / (D * k_max)
        if UpdateProbability > random.random():
            players[x].newStrategy = players[y].strategy
            return
    players[x].newStrategy = players[x].strategy


# @jit(float64(Graph, string, float64))
# @ti.func()
@jit
def EvolutionGameStep(NOCs, Game, bORr):  # 一轮演化过程
    _PayOff = PayOff(bORr)

    # 博弈收益
    for _id in range(N):
        if np.count_nonzero(NOCs[_id]) != 0:
            for friend in list(np.nonzero(NOCs[_id])):
                players[_id].AccPayOffs += play(_id, friend, _PayOff)
    # 策略更新
    for _id in range(N):
        if np.count_nonzero(NOCs[_id]) != 0:
            friend = random.choice(list(np.nonzero(NOCs[_id])))
            strategyUpdate(_id, friend, _PayOff, Game, NOCs)

    Temp = 0
    for _id in range(N):
        players[_id].AccPayOffs = 0  # 每轮都要清零一次
        players[_id].strategy = players[_id].newStrategy
        if players[_id].strategy:
            Temp += 1
    # output2File("output.txt", "a", "TempCooperators: {}".format(Temp))
    return Temp / N
    # pass


# @jit(float64(Graph, string, float64, float64, float64))
# @ti.kernel()
@njit
def EvolutionGameProcess(Mat, Game, g, bORr, prob):
    fc = 0.
    for _ in range(EG_Rounds):
        GTemp = 0.
        for _i in range(G1 + G2):
            snapshot = Mat.copy()
            [rows, cols] = snapshot.shape
            for x in range(rows):
                for y in range(cols):
                    if prob > random.random():
                        snapshot[x, y] = snapshot[y, x] = 0
            for _j in range(_i, min(_i + g, G1 + G2)):
                mean = EvolutionGameStep(snapshot, Game, bORr)
                if _j > G1:
                    GTemp = GTemp + mean
            _i += g - 1
        GTemp = GTemp / G2
        fc = fc + GTemp
    fc = fc / EG_Rounds
    return fc
