#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
1.图：深度优先、广度优先
2.排序：比较器容器
3.设计题
4.滑动窗口、双指针
5.前缀和
6.回溯
7.二分
8.贪心
"""

# 图
from typing import List


class Graph:
    def dfs(self, node):
        if not node:
            return
        visited = set(node)
        stack = [node]
        while stack:
            cur = stack.pop()
            for c in cur:
                if c not in visited:
                    stack.append(cur)
                    stack.append(c)
                    visited.add(c)

    def bfs(self, node):
        from queue import Queue
        if not node:
            return
        queue = Queue()
        visited = set()
        queue.put(node)
        visited.add(node)
        while queue:
            cur = queue.get()
            for c in cur:
                if c not in visited:
                    visited.add(c)
                    queue.put(c)


# 矩阵题
class BoardWithDfs:
    def solve(self, board: List[List[str]]):
        row, col = len(board), len(board[0])
        visited = set()

        def dfs(i, j):
            board[i][j] = '#'
            visited.add((i, j))
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = i + x, j + y
                if (nx, ny) not in visited and 0 <= nx < row and 0 <= ny < col and board[nx][ny] != '#':
                    dfs(nx, ny)
                    visited.add((nx, ny))

        def bfs(i, j):
            queue = []
            queue.append((i, j))
            visited.add((i, j))
            while queue:
                i, j = queue.pop(0)
                board[i][j] = '#'
                for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nx, ny = i + x, j + y
                    if (nx, ny) not in visited and 0 <= nx < row and 0 <= ny < col and board[nx][ny] != '#':
                        queue.append((nx, ny))
                        visited.add((nx, ny))

        for i in range(row):
            for j in range(col):
                dfs(i, j)
                bfs(i, j)


'''
排序
'''
from sortedcontainers import SortedList, SortedSet, SortedDict

ls = [10, 10, 5, 3, 2, 4, 1]
sl = SortedList(ls)
ss = SortedSet(ls)
sd = SortedDict()

print(sl)
print(ss)
sd['c'] = 2
sd['a'] = 3
sd['b'] = 1
print(sd)


class SortClass:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight


# 自定义排序
def cmp(sort_class: SortClass):
    return sort_class.name, sort_class.age, sort_class.weight


'''
滑动窗口
'''

# def slideWindow(nums: List[str]):
#     left = 0
#     ans = []
#     for right in range(len(nums)):
#         更新窗内信息
#         while 窗口不符合题意:
#             扩展或者收缩窗口
#             left += 1
#     return ans

# def findSubArray(nums):
#     N = len(nums) # 数组/字符串长度
#     left, right = 0, 0 # 双指针，表示当前遍历的区间[left, right]，闭区间
#     sums = 0 # 用于统计 子数组/子区间 是否有效，根据题目可能会改成求和/计数
#     res = 0 # 保存最大的满足题目要求的 子数组/子串 长度
#     while right < N: # 当右边的指针没有搜索到 数组/字符串 的结尾
#         sums += nums[right] # 增加当前右边指针的数字/字符的求和/计数
#         while 区间[left, right]不符合题意：# 此时需要一直移动左指针，直至找到一个符合题意的区间
#             sums -= nums[left] # 移动左指针前需要从counter中减少left位置字符的求和/计数
#             left += 1 # 真正的移动左指针，注意不能跟上面一行代码写反
#             # 到 while 结束时，我们找到了一个符合题意要求的 子数组/子串
#         res = max(res, right - left + 1) # 需要更新结果
#         right += 1 # 移动右指针，去探索新的区间
#     return res

'''
前缀和
'''
from itertools import accumulate

ls = [1, 2, 3, 4, 5]
print(list(accumulate(ls)))
