#!/usr/bin/python3
# -*- coding:utf-8 -*-
import heapq
from typing import List


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # 按空闲时间和序号排序
        arr = [[j, i] for i, j in enumerate(servers)]
        arr.sort(key=lambda x: (x[0], x[1]))
        m = len(tasks)
        heap1 = []
        heap2 = []
        for i, h in enumerate(servers):
            heapq.heappush(heap1, [h, i])
        # 如果当前任务时间《=服务器时间，则当前服务器即可处理完毕，否则需要一直处理
        res = [-1] * m
        for i, t in enumerate(tasks):
            while heap2 and heap2[0][0] <= i:
                end, w, index = heapq.heappop(heap2)
                # 重新加入空闲队列
                heapq.heappush(heap1, [w, index])
            if heap1:
                # 获取空闲队列
                w, index = heapq.heappop(heap1)
                res[i] = index
                heapq.heappush(heap2, [i + t, w, index])
            else:
                # 等最近的服务器使用完
                end, w, index = heapq.heappop(heap2)
                res[i] = index
                heapq.heappush(heap2, [end + t, w, index])
        return res


if __name__ == '__main__':
    s = Solution()
    servers = [3, 3, 2]
    tasks = [1, 2, 3, 2, 1, 2]
    # tasks = [5, 5, 5]
    print(s.assignTasks(servers, tasks))
