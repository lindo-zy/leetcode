#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class TrieNode:
    def __init__(self):
        self.child = {}
        self.isWord = False
        self.weight = -1


class WordFilter:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for weight, word in enumerate(words):  # apple
            tmp = word + '#' + word  # apple#apple
            for i in range(len(word) + 1):
                rt = self.root
                for c in tmp[i:]:  # 比如ple#apple
                    if c not in rt.child:
                        rt.child[c] = TrieNode()
                    rt = rt.child[c]
                    rt.weight = weight

    def f(self, prefix: str, suffix: str) -> int:
        rt = self.root
        tmp = suffix + '#' + prefix
        for c in tmp:
            if c not in rt.child:
                return -1
            rt = rt.child[c]
        return rt.weight


wordFilter = WordFilter(["apple"])
wordFilter.f("a", "e")  # 返回 0 ，因为下标为 0 的单词的 prefix = "a" 且 suffix = 'e" 。
