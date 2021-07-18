#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import deque


class FrontMiddleBackQueue:

    def __init__(self):
        self.fmb_queue = deque()

    def pushFront(self, val: int) -> None:
        self.fmb_queue.appendleft(val)

    def pushMiddle(self, val: int) -> None:
        self.fmb_queue.insert(len(self.fmb_queue) // 2, val)

    def pushBack(self, val: int) -> None:
        self.fmb_queue.append(val)

    def popFront(self) -> int:
        if self.fmb_queue:
            return self.fmb_queue.popleft()
        return -1

    def popMiddle(self) -> int:
        if self.fmb_queue:
            val = self.fmb_queue[(len(self.fmb_queue) - 1) // 2]
            del self.fmb_queue[(len(self.fmb_queue) - 1) // 2]
            return val
        return -1

    def popBack(self) -> int:
        if self.fmb_queue:
            return self.fmb_queue.pop()
        return -1


q = FrontMiddleBackQueue()
q.pushFront(1)  # [1]
print(q.fmb_queue)
q.pushBack(2)  # [1, 2]
print(q.fmb_queue)
q.pushMiddle(3)  # [1, 3, 2]
print(q.fmb_queue)
q.pushMiddle(4)  # [1, 4, 3, 2]
print(q.fmb_queue)
q.popFront()  # 返回 1 -> [4, 3, 2]
print(q.fmb_queue)
q.popMiddle()  # 返回 3 -> [4, 2]
print(q.fmb_queue)
print(q.popMiddle())  # 返回 4 -> [2]
print(q.fmb_queue)
print(q.popBack())  # 返回 2 -> []
print(q.fmb_queue)
q.popFront()  # 返回 -1 -> [] （队列为空）
print(q.fmb_queue)
