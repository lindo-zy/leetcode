#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        dp = [0 for _ in range(len(box))]
        box.sort()

        for i in range(len(box)):
            dp[i] = box[i][2]
            for j in range(i):
                if box[j][0] < box[i][0] and box[j][1] < box[i][1] and box[j][2] < box[i][2]:
                    dp[i] = max(dp[i], dp[j] + box[i][2])
        print(dp)
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    box = [[1, 1, 1], [2, 3, 4], [2, 6, 7], [3, 4, 5]]
    print(s.pileBox(box))
