#!/usr/bin/python3
# -*- coding:utf-8 -*-
import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = collections.defaultdict(list)  # 邻接表
        for f, t in tickets:
            d[f] += [t]  # 路径存进邻接表

        for f in d:
            d[f].sort()  # 邻接表排序

        ans = []

        def dfs(f):  # 深搜函数
            while d[f]:
                dfs(d[f].pop(0))  # 路径检索
            ans.insert(0, f)  # 放在最前

        dfs('JFK')
        return ans


if __name__ == '__main__':
    s = Solution()
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    # ['JFK', 'SFO', 'ATL', 'JFK', 'ATL', 'SFO']
    # ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']
    print(s.findItinerary(tickets))
