#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        ans, d = [], {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
        for i in range(len(s)):
            ops, tmp = s[i:], 0
            x, y = startPos[0], startPos[1]  # 初始坐标
            for op in ops:
                x, y = x + d[op][0], y + d[op][1]
                if 0 <= x < n and 0 <= y < n:
                    tmp += 1  # 未出界+1
                else:
                    break  # 出界直接停止
            ans.append(tmp)
        return ans


if __name__ == '__main__':
    sn = Solution()
    n = 3
    startPos = [0, 1]
    s = "RRDDLU"  # [1,5,4,3,1,0]
    print(sn.executeInstructions(n, startPos, s))
