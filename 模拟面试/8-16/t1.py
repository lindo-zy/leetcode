#!/usr/bin/python3
# -*- coding:utf-8 -*-
from itertools import groupby
from typing import List


class Solution:
    def halfQuestions(self, questions: List[int]) -> int:
        # 人数
        n = len(questions) // 2
        # 贪心，按多的选，选完再选次多的，满足n即可
        cnt = 0
        questions.sort()
        nums = []
        for i, item in groupby(questions):
            nums.append([i, len(list(item))])
        nums.sort(key=lambda x: x[1], reverse=True)
        for i in range(len(nums)):
            n -= nums[i][1]
            cnt += 1
            if n <= 0:
                return cnt


if __name__ == '__main__':
    s = Solution()
    questions = [1, 5, 1, 3, 4, 5, 2, 5, 3, 3, 8, 6]
    questions = [1000, 1000]
    print(s.halfQuestions(questions))
