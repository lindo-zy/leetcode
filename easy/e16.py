#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        r, p = '', 0
        d = len(b) - len(a)
        a = '0' * d + a
        b = '0' * -d + b
        for i, j in zip(a[::-1], b[::-1]):
            s = int(i) + int(j) + p
            r = str(s % 2) + r
            p = s // 2

        return '1' + r if p else r


if __name__ == '__main__':
    s = Solution2()
    a = '11'
    b = '1'  # 01
    a = '1010'
    b = '1011'
    result = s.addBinary(a, b)
    print(result)  # 100 10101
