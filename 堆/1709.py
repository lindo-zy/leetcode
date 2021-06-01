#!/usr/bin/python3
# -*- coding:utf-8 -*-
import heapq


class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        heap = [1]
        for i in range(k):
            res = heapq.heappop(heap)
            while heap and res == heap[0]:  # 去除重复元素
                heapq.heappop(heap)
            heapq.heappush(heap, res * 3)
            heapq.heappush(heap, res * 5)
            heapq.heappush(heap, res * 7)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.getKthMagicNumber(5))
