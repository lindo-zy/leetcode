#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        right = 0
        win_len = 4
        cnt = 0
        while right + win_len <= n:
            temp = win_len - len(set(s[right:right + win_len]))
            cnt += temp
            right += win_len
        return cnt


if __name__ == '__main__':
    sn = Solution()
    # s = "QQQW"
    # s = "QQQQ"
    # s = "QWER"
    s = "WWEQERQWQWWRWWERQWEQ"
    print(sn.balancedString(s))
