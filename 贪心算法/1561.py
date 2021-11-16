#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import deque
from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        queue = deque(piles)
        # alice取最大的，Bob取最小的，我取第二大的即可
        ans = 0
        while queue:
            queue.pop()
            ans += queue.pop()
            queue.popleft()
        return ans


if __name__ == '__main__':
    s = Solution()
    piles = [2, 4, 1, 2, 7, 8]
    # piles = [9, 8, 7, 6, 5, 1, 2, 3, 4]
    print(s.maxCoins(piles))
