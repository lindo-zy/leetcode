#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        s1 = min(strs)
        s2 = max(strs)

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return s2[:i]
        return s1

class Solution2:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        ss = list(map(set, zip(*strs)))
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res


if __name__ == '__main__':
    s = Solution()
    strs = ["dog", "racecar", "car"]
    strs = ["flower", "flow", "flight"]
    result = s.longestCommonPrefix(strs)
    print(result)
