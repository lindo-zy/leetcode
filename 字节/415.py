#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry, res = 0, []

        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0

            s = carry + n1 + n2

            if s >= 10:
                carry = 1
                res.append(str(s - 10))
            else:
                carry = 0
                res.append(str(s))
            i -= 1
            j -= 1
        if carry == 1:
            res.append('1')

        return ''.join(res[::-1])


if __name__ == '__main__':
    sn = Solution()
    num1 = "11"
    num2 = "123"
    print(sn.addStrings(num1, num2))
