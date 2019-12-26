#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Solution:
    def romanToInt(self, s: str) -> int:
        ds = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for i in range(len(s)):
            if i < len(s) - 1 and ds[s[i]] < ds[s[i + 1]]:
                num -= ds[s[i]]
            else:
                num += ds[s[i]]

        if 1 <= num <= 3999:
            return num


if __name__ == '__main__':
    sn = Solution()
    s = 'LVIII'  # 58 L=50 V=5 III=3
    s = 'MCMXCIV'  # 1994 M=1000 CM=900 XC=90 IV=4
    # s = 'MMMCMXCIX'  # 3999 MMMCMXCIX 3000=MMM CM=900 XC=90 IC=9
    result = sn.romanToInt(s)
    print(result)
