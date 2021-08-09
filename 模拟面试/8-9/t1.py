#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = int(''.join(map(str, digits))) + 1
        return list(map(int, str(s)))


if __name__ == '__main__':
    s = Solution()
    digits = [1, 2, 3]
    print(s.plusOne(digits))
