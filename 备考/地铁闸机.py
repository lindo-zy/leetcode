#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import deque


class Solution:
    def station(self, arr_time, directs):
        # 出站队列
        out_queue = deque()
        # 入站队列
        in_queue = deque()
        # 预处理
        n = len(arr_time)
        for i in range(n):
            if directs[i] == 1:
                out_queue.append([arr_time[i], i])
            else:
                in_queue.append([arr_time[i], i])
        cur_time = 0
        ans = [0] * n
        while out_queue or in_queue:
            out = False
            # 先出站
            while out_queue and out_queue[0][0] <= cur_time:
                index = out_queue.popleft()[1]
                ans[index] = cur_time
                cur_time += 1
                out = True
            # 后入站
            while in_queue and in_queue[0][0] <= cur_time:
                index = in_queue.popleft()[1]
                ans[index] = cur_time
                cur_time += 1
                out = True
            if not out:
                cur_time += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    arr_time = [2, 2, 2, 2, 3, 3, 5, 5, 20, 20]
    directs = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1]
    # [6,2,3,7,8,4,5,9,21,20]
    print(s.station(arr_time, directs))
