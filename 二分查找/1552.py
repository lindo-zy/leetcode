#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        # 特殊情况，直接输出
        if m == 2:
            return abs(max(position) - min(position))

        left, right = 1, position[-1] - position[0]

        ans = 0

        def check(mid):
            # 挑选M个球，使得2数之间的差值最大
            cnt = 1
            first = position[0]
            for p in position:
                if p - first >= mid:
                    first = p
                    cnt += 1
            return cnt >= m

        # 求最小
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid
        return ans


if __name__ == '__main__':
    s = Solution()
    position = [1, 2, 3, 4, 7]
    m = 3

    position = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = 4
    print(s.maxDistance(position, m))
