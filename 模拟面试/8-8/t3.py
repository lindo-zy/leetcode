#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0
        for i in s:
            if i == '(':
                depth = depth + 1
                max_depth = max(depth, max_depth)
            elif i == ')':
                depth = depth - 1
        return max_depth


if __name__ == '__main__':
    sn = Solution()
    s = "(1)+((2))+(((3)))"
    # s = "(1+(2*3)+((8)/4))+1"
    # s = "(1+2)/(5+((4-9+8)*((1+8+(5*7)*4)/(7+9-5)))/(7/3-8-4-8))"
    print(sn.maxDepth(s))
