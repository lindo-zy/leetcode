#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Solution(object):
    def numSubarraysWithSum(self, A, S):
        from collections import defaultdict
        dct, pre, res = defaultdict(int), 0, 0
        dct[0] = 1
        for n in nums:
            pre += n  # 前缀和
            res += dct[pre - goal]
            dct[pre] += 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 0, 1, 0, 1]  # 4
    goal = 2
    # nums = [0, 0, 0, 0, 0]
    # goal = 0
    print(s.numSubarraysWithSum(nums, goal))
