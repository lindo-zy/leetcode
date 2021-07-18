#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Leaderboard:

    def __init__(self):
        self.dic = {}

    def addScore(self, playerId: int, score: int) -> None:
        self.dic[playerId] = self.dic.get(playerId, 0) + score

    def top(self, K: int) -> int:
        s = sorted([v for v in self.dic.values()], reverse=True)
        return sum(s[:K])

    def reset(self, playerId: int) -> None:
        self.dic[playerId] = 0


leaderboard = Leaderboard()
leaderboard.addScore(1, 73)  # leaderboard = [[1,73]]
leaderboard.addScore(2, 56)  # leaderboard = [[1,73],[2,56]]
leaderboard.addScore(3, 39)  # leaderboard = [[1,73],[2,56],[3,39]]
leaderboard.addScore(4, 51)  # leaderboard = [[1,73],[2,56],[3,39],[4,51]]
leaderboard.addScore(5, 4)  # leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]]
leaderboard.top(1)  # returns 73
leaderboard.reset(1)  # leaderboard = [[2,56],[3,39],[4,51],[5,4]]
leaderboard.reset(2)  # leaderboard = [[3,39],[4,51],[5,4]]
leaderboard.addScore(2, 51)  # leaderboard = [[2,51],[3,39],[4,51],[5,4]]
leaderboard.top(3)  # returns 141 = 51 + 51 + 39
