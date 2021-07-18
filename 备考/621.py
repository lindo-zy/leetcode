#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 计算当前任务频次
        ct = Counter(tasks)
        # 取出最长任务个数
        nbucket = ct.most_common(1)[0][1]
        # 计算最后一个桶内任务占用的长度
        last_bucket_size = list(ct.values()).count(nbucket)
        # 计算公式：（最长任务-1）*（间隔+1）+最后一个桶任务长度
        res = (nbucket - 1) * (n + 1) + last_bucket_size
        # 如果不满足上述公式，则为任务长度
        return max(res, len(tasks))


if __name__ == '__main__':
    s = Solution()
    tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n = 2
    print(s.leastInterval(tasks, n))
