#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(' ')
        n = len(sorted(words, key=lambda x: len(x))[-1])
        for i in range(len(words)):
            words[i] += (n - len(words[i])) * ' '
        res = []
        for j in range(n):
            res.append(''.join(list(k[j] for k in words)).lstrip().rstrip())
        return res


if __name__ == '__main__':
    sn = Solution()
    s = "CONTEST IS COMING"
    print(sn.printVertically(s))
