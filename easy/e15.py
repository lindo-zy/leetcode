#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def plusOne(self, digits):
        return list(map(int, str(int(''.join([str(i) for i in digits])) + 1)))


if __name__ == '__main__':
    s = Solution()
    digits = [1, 2, 3]  # [1,2,4]
    digits = [4, 3, 2, 1]  # [4,3,2,2]
    # digits = [0]  # [1]
    # digits = [9, 9, 9]  # [1,0,0,0]
    result = s.plusOne(digits)
    print(result)
