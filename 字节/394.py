#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def decodeString(self, s: str) -> str:
        # 记录当前字符串
        res = ''
        # 记录当前的数字
        num = ''
        st = []
        for c in s:
            if c.isdigit():
                num += c
            elif c == '[':
                st.append((res, int(num)))
                res, num = '', ''
            elif c == ']':
                top = st.pop()
                res = top[0] + res * top[1]
            else:
                res += c

        return res


if __name__ == '__main__':
    sn = Solution()
    s = "13[a2[c]]"
    print(sn.decodeString(s))
