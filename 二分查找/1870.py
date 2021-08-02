#!/usr/bin/python3
# -*- coding:utf-8 -*-
import math
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # 时间向上取整
        n = len(dist)

        def check(mid):
            cnt = 0
            for i in range(n - 1):
                cnt += math.ceil(dist[i] / mid)
            cnt += dist[-1] / mid
            return cnt

        # 求解列车的时速
        left, right = 1, 10 ** 9
        while left < right:
            mid = (left + right) // 2
            if check(mid) > hour:
                left = mid + 1
            else:
                right = mid
        # 后处理
        if check(left) <= hour:
            return left
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    dist = [1, 1, 100000]
    hour = 2.01
    print(s.minSpeedOnTime(dist, hour))
