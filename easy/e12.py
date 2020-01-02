#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def countAndSay(self, n: int) -> str:
        if 1 <= n <= 30:
            pass

    def func(self, n):
        if n == 1:
            return 1
        else:
            return self.func(n - 1)


if __name__ == '__main__':
    s = Solution()
    n = 6  # 输入项数
    result = s.countAndSay(n)  # 返回数字
    print(result)
