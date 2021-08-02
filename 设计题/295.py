#!/usr/bin/python3
# -*- coding:utf-8 -*-
from sortedcontainers import SortedList


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = SortedList()

    def addNum(self, num: int) -> None:
        self.nums.add(num)

    def findMedian(self) -> float:
        if len(self.nums) & 1 == 0:
            mid = len(self.nums) + 1 >> 1
            return (self.nums[mid] + self.nums[mid + 1]) / 2
        else:
            mid = len(self.nums) >> 1
            return self.nums[mid] / 2
