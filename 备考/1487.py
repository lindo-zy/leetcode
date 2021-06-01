#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        d, ans = {}, []
        for name in names:
            s = name
            while s in d:
                s = f'{name}({d[name]})'
                d[name] += 1
            d[s] = 1
            ans.append(s)
        return ans


if __name__ == '__main__':
    s = Solution()
# names = ["pes", "fifa", "gta", "pes(2019)"]
names = ["gta", "gta(1)", "gta", "avalon"]
print(s.getFolderNames(names))
