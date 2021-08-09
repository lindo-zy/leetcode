#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        n = len(milestones)
        milestones.append(0)
        milestones.sort(reverse=True)
        print(milestones)
        res = 0
        cur = milestones[0]
        for i in range(1, n):
            if cur == milestones[i]:
                res += cur * 2
                cur = milestones[i + 1]
            else:
                res += min(cur, milestones[i]) * 2
                cur = abs(cur - milestones[i])

        return res


if __name__ == '__main__':
    s = Solution()
    milestones = [5, 7, 5, 7, 9, 7]  # 40
    milestones = [5, 5, 1]  # 11
    print(s.numberOfWeeks(milestones))
