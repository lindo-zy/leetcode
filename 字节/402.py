#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for d in num:
            while st and k and st[-1] > d:
                st.pop()
                k -= 1
            st.append(d)
        if k > 0:
            st = st[:-k]
        return ''.join(st).lstrip('0') or '0'


if __name__ == '__main__':
    sn = Solution()
    num = "1432219"
    k = 3
    num = "10200"
    k = 1
    print(sn.removeKdigits(num, k))
