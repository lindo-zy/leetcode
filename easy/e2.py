#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def reverse(self, x: int) -> int:
        x_min = -2 ** 31
        x_max = 2 ** 31 - 1

        if str(x)[0] == '-':
            result = int('-' + str(x)[1:][::-1])
        else:
            result = int(str(x)[::-1])
        if x_min <= result <= x_max:
            return result
        return 0


if __name__ == '__main__':
    s = Solution()
    x = 1534236469
    x = 123
    x = 120
    x = -120
    result = s.reverse(x)
    print(result)

