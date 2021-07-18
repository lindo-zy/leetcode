#!/usr/bin/python3
# -*- coding:utf-8 -*-
import re
from typing import List


class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        res, S2 = [0] * len(S), ""
        # 正则识别非overlap的所有word的位置
        for word in words:
            for m in re.finditer('(?={0})'.format(word), S):
                # 所有符合条件的char赋值为1
                res[m.start():m.start() + len(word)] = [1] * len(word)
        # 给所有赋值为1的char两边加上bold的括号
        for k, v in enumerate(res):
            S2 += "<b>" + S[k] + "</b>" if v else S[k]
        print(S2)
        # 把成对的冗余括号消去
        return S2.replace("</b><b>", "")


if __name__ == '__main__':
    sn = Solution()
    s = "aaabbcc"
    words = ["aaa", "aab", "bc"]
    print(sn.boldWords(words, s))
