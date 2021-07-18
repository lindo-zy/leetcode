#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: (-len(x), x))

        def dfs(w, words):
            if not w: return True
            for i, nxt in enumerate(words):
                if nxt == w[:len(nxt)]:
                    if dfs(w[len(nxt):], words):
                        return True
            return False

        for i, word in enumerate(words):
            if dfs(word, words[i + 1:]):
                return word

        return ''


if __name__ == '__main__':
    s = Solution()
    words = ["cat", "banana", "dog", "nana", "walk", "walker", "dogwalker"]
    print(s.longestWord(words))
