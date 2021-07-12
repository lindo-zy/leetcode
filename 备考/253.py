#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = [(iv[0], 1) for iv in intervals] + [(iv[1], -1) for iv in intervals]
        events.sort()
        ans = cur = 0
        for _, e in events:
            cur += e
            ans = max(ans, cur)
        return ans


if __name__ == '__main__':
    s = Solution()
    intervals = [[0, 30], [5, 10], [15, 20]]
    # intervals = [[7, 10], [2, 4]]
    print(s.minMeetingRooms(intervals))
