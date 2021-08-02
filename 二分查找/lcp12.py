#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        n = len(time)
        if n <= m:
            return 0

        # 预处理，排除最大的m个值

        def check(mid):
            load, save, days = 0, 0, 1  # 用save表示最耗时的题目，也就是节省的时间
            for weight in time:
                if weight > save:  # 寻找最耗时的题目，省去的时间是该题的耗时
                    save = weight
                if load + weight - save > mid:  # 判别是否超出一天的最大耗时限制，要减去求助节省的时间
                    days += 1
                    load = weight
                    save = weight  # 新的一天，另起炉灶，最耗时的题目也要重新数起
                else:
                    load += weight
            return days > m

        # 定义时间范围
        left, right = 0, sum(time)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid
        # 后处理
        return left


if __name__ == '__main__':
    s = Solution()
    time = [1, 2, 7, 4, 7]
    m = 2  # 4
    print(s.minTime(time, m))
