#!/usr/bin/python3
# -*- coding:utf-8 -*-
from operator import mul, floordiv, sub


class Operations:

    def __init__(self):
        pass

    def minus(self, a: int, b: int) -> int:
        return sub(a, b)

    def multiply(self, a: int, b: int) -> int:
        return mul(a, b)

    def divide(self, a: int, b: int) -> int:
        return floordiv(a, b)

# Your Operations object will be instantiated and called as such:
# obj = Operations()
# param_1 = obj.minus(a,b)
# param_2 = obj.multiply(a,b)
# param_3 = obj.divide(a,b)
