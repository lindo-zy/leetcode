#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        cnt = 0
        for i, j in zip(list(s), list(t)):
            print(ord(j) - ord(i))
            cnt += (ord(j) - ord(i))
        print(cnt)
        return cnt <= k


if __name__ == '__main__':
    sn = Solution()
    s = "input"
    t = "ouput"
    k = 9

    # s = "aab"
    # t = "bbb"
    # k = 27
    print(sn.canConvertString(s, t, k))
