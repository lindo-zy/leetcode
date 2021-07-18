#!/usr/bin/python3
# -*- coding:utf-8 -*-
import numpy as np


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        return np.median(self.arr)


m = MedianFinder()
m.addNum(1)
m.addNum(2)
print(m.findMedian())
m.addNum(3)
print(m.findMedian())
