#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            temp = str(x)
            if temp == temp[::-1]:
                return True
            return False


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        div = 1
        while x / div >= 10:
            div *= 10

        while x > 0:
            left = x // div
            right = x % 10
            if left != right:
                return False
            x = (x % div) // 10
            div //= 100
        return True
