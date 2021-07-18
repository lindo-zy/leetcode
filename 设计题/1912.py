#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import defaultdict
from typing import List

from sortedcontainers import SortedList


class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.n = n
        self.movies = defaultdict(SortedList)
        # 商店，仅用来记录电影和对应的价格
        self.shops = defaultdict(dict)
        self.renting = SortedList([])
        for shop, movie, price in entries:
            self.movies[movie].add((price, shop))
            self.shops[shop][movie] = price

    def search(self, movie: int) -> List[int]:
        return [i[1] for i in list(self.movies[movie][:5])]

    def rent(self, shop: int, movie: int) -> None:
        price = self.shops[shop][movie]
        self.movies[movie].remove((price, shop))
        self.renting.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.shops[shop][movie]
        self.movies[movie].add((price, shop))
        self.renting.remove((price, shop, movie))

    def report(self) -> List[List[int]]:
        return [[x, y] for _, x, y in self.renting[:5]]


movieRentingSystem = MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]])

print(movieRentingSystem.search(1))  # 返回 [1, 0, 2] ，商店 1，0 和 2 有未借出的 ID 为 1 的电影。商店 1 最便宜，商店 0 和 2 价格相同，所以按商店编号排序。

print(movieRentingSystem.rent(0, 1))  # 从商店 0 借出电影 1 。现在商店 0 未借出电影编号为 [2,3] 。
print(movieRentingSystem.rent(1, 2))  # 从商店 1 借出电影 2 。现在商店 1 未借出的电影编号为 [1] 。
print(movieRentingSystem.report())  # 返回 [[0, 1], [1, 2]] 。商店 0 借出的电影 1 最便宜，然后是商店 1 借出的电影 2 。
print(movieRentingSystem.drop(1, 2))  # 在商店 1 返还电影 2 。现在商店 1 未借出的电影编号为 [1,2] 。
print(movieRentingSystem.search(2))  # 返回 [0, 1] 。商店 0 和 1 有未借出的 ID 为 2 的电影。商店 0 最便宜，然后是商店 1
