#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        st = []
        for it in intervals:
            if st and it[0] <= st[-1][1]:
                st[-1][1] = max(it[1], st[-1][1])
            else:
                st.append(it)
        return st


if __name__ == '__main__':
    sn = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(sn.merge(intervals))
