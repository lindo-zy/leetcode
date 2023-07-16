#!/usr/bin/python3
# -*- coding:utf-8 -*-
class MinStack:

    def __init__(self):
        # 普通栈
        self.st = []
        # 存最小值
        self.min_st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.min_st or val <= self.min_st[-1]:
            self.min_st.append(val)

    def pop(self) -> None:
        if self.st.pop() == self.min_st[-1]:
            self.min_st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1]
