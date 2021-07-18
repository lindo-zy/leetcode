#!/usr/bin/python3
# -*- coding:utf-8 -*-
import re
from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        r = re.compile(f'{"[a-z]*".join(["", *pattern, ""])}$')
        ans = []
        for i in map(r.match, queries):
            if i:
                ans.append(True)
            else:
                ans.append(False)
        return ans


if __name__ == '__main__':
    s = Solution()
    queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
    pattern = "FB"
    print(s.camelMatch(queries, pattern))
