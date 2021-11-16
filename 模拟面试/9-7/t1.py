#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # for i in s:
        #     s = "".join(s.split(i * k))
        # return s
        n = len(s)
        stack = []
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            elif stack[-1][1] + 1 < k:
                stack[-1][1] += 1
            else:
                stack.pop()
        ans = ""
        for c, l in stack:
            ans += c * l
        return ans


if __name__ == '__main__':
    sn = Solution()
    s = "deeedbbcccbdaa"
    k = 3
    # s = "pbbcggttciiippooaais"
    # k = 2
    print(sn.removeDuplicates(s, k))
