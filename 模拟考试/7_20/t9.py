#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import defaultdict
from functools import reduce, lru_cache
from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def Trie():
            return defaultdict(Trie)

        @lru_cache(None)
        def is_concat(w, cnt=0):
            if not w and cnt > 1:
                return True
            cur_trie = trie
            for i, c in enumerate(w):
                # min(cnt+1, 2)剪掉不必要的lru缓存
                if '$' in cur_trie[c] and is_concat(w[i + 1:], min(cnt + 1, 2)):
                    return True
                cur_trie = cur_trie[c]
            return False

        trie = Trie()
        for w in words:
            # 完整的单词以 $ 字符结尾
            reduce(dict.__getitem__, w + '$', trie)

        return [w for w in words if is_concat(w)]


if __name__ == '__main__':
    s = Solution()
    words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
    print(s.findAllConcatenatedWordsInADict(words))
