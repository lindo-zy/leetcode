from typing import List
from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @lru_cache
        def dfs(s):
            if not s:
                return True
            res = False

            for w in wordDict:
                if s.startswith(w):
                    res |= dfs(s[len(w):])

            return res

        return dfs(s)
