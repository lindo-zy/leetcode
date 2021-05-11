#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans = [""]
        for k in digits:
            ans = [i + j for i in ans for j in dic[k]]
        return ans


if __name__ == '__main__':
    s = Solution()
    digits = "23"
    print(s.letterCombinations(digits))
