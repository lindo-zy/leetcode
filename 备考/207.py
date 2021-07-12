#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        # 构建图
        for x, y in prerequisites:
            graph[y].append(x)

        def dfs(i, begin_visited):
            if i in begin_visited:
                return False
            if i in visited:
                return True
            visited.add(i)
            begin_visited.add(i)
            for j in graph[i]:
                if not dfs(j, begin_visited):
                    return False
            begin_visited.remove(i)
            return True

        for i in range(numCourses):
            if i in visited:
                continue
            if not dfs(i, set()):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    print(s.canFinish(numCourses, prerequisites))
