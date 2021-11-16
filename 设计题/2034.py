#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import defaultdict


class StockPrice:

    def __init__(self):
        # 记录时间戳对应的价格
        self.record = defaultdict(int)
        # 记录时间戳添加顺序
        self.order = SortedList()

    def update(self, timestamp: int, price: int) -> None:
        # 更新为最新的价格
        self.record[timestamp] = price
        if timestamp not in self.order:
            self.order.add(timestamp)

    def current(self) -> int:
        # 返回当前时间的价格
        return self.record.get(self.order[-1])

    def maximum(self) -> int:
        # 获取当前股票的最高的价格
        price = float('-inf')
        for k, v in self.record.items():
            price = max(price, v)
        return price

    def minimum(self) -> int:
        # 获取当前股票最低的价格
        price = float('inf')
        for k, v in self.record.items():
            price = min(price, v)
        return price


from sortedcontainers import SortedList


class StockPrice:

    def __init__(self):
        self.time = {}
        self.price = SortedList()
        self.cur = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp > self.cur:
            self.cur = timestamp
        if timestamp in self.time:
            self.price.remove(self.time[timestamp])

        self.time[timestamp] = price
        self.price.add(price)

    def current(self) -> int:
        return self.time[self.cur]

    def maximum(self) -> int:
        return self.price[-1]

    def minimum(self) -> int:
        return self.price[0]


stockPrice = StockPrice()  #
print(stockPrice.update(1, 10))  # // 时间戳为 [1] ，对应的股票价格为 [10] 。
print(stockPrice.update(2, 5))  # // 时间戳为 [1,2] ，对应的股票价格为 [10,5] 。
print(stockPrice.current())  # // 返回 5 ，最新时间戳为 2 ，对应价格为 5 。
print(stockPrice.maximum())  # // 返回 10 ，最高价格的时间戳为 1 ，价格为 10 。
print(stockPrice.update(1, 3))  # // 之前时间戳为 1 的价格错误，价格更新为 3 。// 时间戳为 [1,2] ，对应股票价格为 [3,5] 。
print(stockPrice.maximum())  # // 返回 5 ，更正后最高价格为 5 。
print(stockPrice.update(4, 2))  # // 时间戳为 [1,2,4] ，对应价格为 [3,5,2] 。
print(stockPrice.minimum())  # // 返回 2 ，最低价格时间戳为 4 ，价格为 2 。
