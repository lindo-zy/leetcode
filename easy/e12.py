#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.bs(self.countAndSay(n - 1))

    def bs(self, string):
        lis = list(string)
        lis.append('0')  # 末尾补一个，方便后续计数
        lis1 = []
        re = 0
        i = 0
        while i < len(lis) - 1:
            if lis[i] != lis[i + 1]:
                lis1.append(str(i + 1 - re))  # 当前计录的值的个数
                lis1.append(lis[i])  # 当前记录的值
                re = i + 1
            i = i + 1
        s = ''.join(lis1)  # 列表转字符串
        return s


if __name__ == '__main__':
    s = Solution()
    n = 4  # 输入项数
    result = s.countAndSay(n)  # 返回数字
    print(result)
