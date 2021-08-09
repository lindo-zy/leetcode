#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Solution:
    def minInsertions(self, s: str) -> int:
        s = s.replace('))', '*')
        needcnt = s.count(')')
        s = s.replace(')', '*')

        while len(ss := s.replace('(*', '')) != len(s):
            s = ss
        return needcnt + len(s) + s.count('(')


if __name__ == '__main__':
    sn = Solution()
    s = "(()))"
    s = ")))))))"
    s = "()()()()()("  # 7
    s = "(()))(()))()())))"  # 4
    # s = "((())))))"  # 0
    print(sn.minInsertions(s))
