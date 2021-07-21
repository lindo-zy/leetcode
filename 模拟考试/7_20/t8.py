#!/usr/bin/python3
# -*- coding:utf-8 -*-
from itertools import product
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ds = {2: 'abc', 3: 'def', 4: "ghi",
              5: 'jkl', 6: 'mno', 7: 'pqrs',
              8: 'tuv', 9: 'wxyz'}
        words = [ds[int(i)] for i in digits]
        return [''.join(i) for i in list(product(*words)) if i]


if __name__ == '__main__':
    s = Solution()
    digits = "234"
    print(s.letterCombinations(digits))
