#!/usr/bin/python3
# -*- coding:utf-8 -*-
import collections
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        hashmap = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                hashmap[word[:i] + '*' + word[i + 1:]].append(word)

        ans = []
        visited = set()
        visited.add(beginWord)

        def dfs(beginWord, temp):
            if beginWord == endWord:
                ans.extend(temp)
                return

            for i in range(len(beginWord)):
                for word in hashmap[beginWord[:i] + '*' + beginWord[i + 1:]]:
                    if word not in visited:
                        visited.add(word)
                        dfs(word, temp + [word])

        dfs(beginWord, [])
        return [beginWord] + ans if ans else ans
