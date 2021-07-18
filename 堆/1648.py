#!/usr/bin/python3
# -*- coding:utf-8 -*-
import heapq
from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        cnt = 0
        # 构建大顶堆
        big_heapq = []
        for num in inventory:
            heapq.heappush(big_heapq, -num)
        s = 0
        while cnt < orders:
            cur = -heapq.heappop(big_heapq)
            s += cur % (10 ** 9 + 7)
            heapq.heappush(big_heapq, (-cur + 1))
            cnt += 1
        return s


if __name__ == '__main__':
    s = Solution()
    inventory = [2, 8, 4, 10, 6]
    orders = 20
    print(s.maxProfit(inventory, orders))
