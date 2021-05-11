#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        record = []
        small = set(small)
        for index, num in enumerate(big):
            if num in small:
                record.append([num, index])
        # 最小窗口为 small的长度
        ans = len(big)
        ds = {}
        left = 0
        right = 0
        for i in range(len(record)):
            if record[i][0] in small:
                ds[record[i][0]] = record[i][1]
            if len(small) == len(ds):
                left_value = min(ds.values())
                right_value = max(ds.values())
                if ans > right_value - left_value:
                    left = left_value
                    right = right_value
                    ans = min(ans, right - left)
        return [left, right]


if __name__ == '__main__':
    s = Solution()
    big = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
    small = [1, 5, 9]
    print(s.shortestSeq(big, small))  # 7 10
