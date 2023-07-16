#!/usr/bin/python3
# -*- coding:utf-8 -*-
class MyQueue:

    def __init__(self):
        # 先进后出
        self.st = []

    def push(self, x: int) -> None:
        self.st.append(x)

    def pop(self) -> int:
        return self.st.pop(0)

    def peek(self) -> int:
        return self.st[0]

    def empty(self) -> bool:
        return not bool(len(self.st))
