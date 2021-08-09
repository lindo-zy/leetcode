#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        # 查找2个子数组，能组成的最大和，且一样
        s = sum(rods)
        ave = s // 2
        print(ave)
        # 如果不存在，则返回0


if __name__ == '__main__':
    s = Solution()
    rods = [1, 2, 3, 6]
    rods = [1, 2, 3, 4, 5, 6]
    print(s.tallestBillboard(rods))
