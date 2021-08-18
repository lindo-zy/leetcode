#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:

        arr = text.split(' ')
        n = len(arr)
        ans = []
        right = 0
        while right < n - 2:
            temp = arr[right:right + 3]
            if temp and temp[0] == first and temp[1] == second:
                ans.append(temp[-1])
            right += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    # text = "alice is a good girl she is a good student"
    # first = "a"
    # second = "good"

    text = "we will we will rock you"
    first = "we"
    second = "will"
    print(s.findOcurrences(text, first, second))
