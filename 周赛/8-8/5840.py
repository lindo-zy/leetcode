#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def minSwaps(self, s: str) -> int:
        res = 0
        cnt = 0
        for c in s:
            if c == '[':
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                res += 1
                cnt += 2

        return res


if __name__ == '__main__':
    sn = Solution()
    s = "]]][[["
    print(sn.minSwaps(s))
