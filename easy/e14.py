#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(' ')  # 去掉末尾空格
        L = s.split(' ')[-1]
        return len(L)


if __name__ == '__main__':
    s = Solution()
    string = 'Hello World'  # 5
    # string = ''  # 0
    string = 'a'  # 1
    result = s.lengthOfLastWord(string)
    print(result)
