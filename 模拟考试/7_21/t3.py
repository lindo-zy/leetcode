#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        s = ''
        res = [False] * len(nums)
        for index, i in enumerate(nums):
            s += str(i)

            if int(s, 2) % 5 == 0:
                res[index] = True

        return res


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 1, 1, 1, 1]
    print(s.prefixesDivBy5(nums))
    # print(int('011', 2))
