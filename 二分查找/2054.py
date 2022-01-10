#!/usr/bin/python3
# -*- coding:utf-8 -*-
import heapq
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        # 按结束时间排序，尽量多选择,最多2个，至少1个
        # events.sort(key=lambda x: x[1])
        # ans = 0
        # x = [0]  # 结束时间
        # y = [0]  # 当前值
        # for i, j, v in events:
        #     ans = max(ans, v + y[bisect.bisect_left(x, i) - 1])
        #     if j == x[-1]:
        #         y[-1] = max(y[-1], v)
        #     elif y[-1] < v:
        #         x.append(j)
        #         y.append(v)
        # return ans

        maxv, res, q = 0, 0, []
        for s, e, v in sorted(events):
            heapq.heappush(q, (e, v))
            while q[0][0] < s:
                maxv = max(maxv, heapq.heappop(q)[1])
            res = max(res, v + maxv)
        return res


if __name__ == '__main__':
    s = Solution()
    events = [[1, 3, 2], [4, 5, 2], [1, 5, 5]]
    print(s.maxTwoEvents(events))
