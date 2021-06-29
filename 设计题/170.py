#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import defaultdict


class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.record = defaultdict(int)

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.record[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for x in self.record.keys():
            temp = value - x
            if x == temp:
                if self.record[x] >= 2:
                    return True
            else:
                if temp in self.record:
                    return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
