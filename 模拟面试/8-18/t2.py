#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        pos = {}

        for i, ch in enumerate(s):
            if ch not in pos:
                pos[ch] = []
            pos[ch].append(i)

        ans = 0
        for pos_list in pos.values():
            for i, mid_pos in enumerate(pos_list):
                pos1 = -1 if i - 1 < 0 else pos_list[i - 1]
                pos2 = len(s) if i + 1 >= len(pos_list) else pos_list[i + 1]
                ans += (mid_pos - pos1) * (pos2 - mid_pos)
                if ans > 1000000007:
                    ans %= 1000000007
        return ans


if __name__ == '__main__':
    sn = Solution()
    s = "ABA"
    print(sn.uniqueLetterString(s))
