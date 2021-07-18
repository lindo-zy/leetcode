#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        curNode = self.trie
        for c in word:
            if c not in curNode:
                curNode[c] = {'pcnt': 0, 'wcnt': 0}
            curNode = curNode[c]
            curNode['pcnt'] += 1
        curNode['wcnt'] += 1

    def countWordsEqualTo(self, word: str) -> int:
        curNode = self.trie
        for c in word:
            if c not in curNode:
                return 0
            curNode = curNode[c]
        return curNode['wcnt']

    def countWordsStartingWith(self, prefix: str) -> int:
        curNode = self.trie
        for c in prefix:
            if c not in curNode: return 0
            curNode = curNode[c]
        return curNode['pcnt']

    def erase(self, word: str) -> None:
        curNode = self.trie
        for c in word:
            curNode = curNode[c]
            curNode['pcnt'] -= 1
        curNode['wcnt'] -= 1


trie = Trie()
print(trie.insert("apple"))  # 插入 "apple"。
print(trie.trie)
print(trie.insert("apple"))  # 插入另一个 "apple"。
print(trie.trie)
print(trie.countWordsEqualTo("apple"))  # 有两个 "apple" 实例，所以返回 2。
print(trie.trie)
print(trie.countWordsStartingWith("app"))  # "app" 是 "apple" 的前缀，所以返回 2。
print(trie.trie)
print(trie.erase("apple"))  # 移除一个 "apple"。
print(trie.trie)
print(trie.countWordsEqualTo("apple"))  # 现在只有一个 "apple" 实例，所以返回 1。
print(trie.trie)
print(trie.countWordsStartingWith("app"))  # 返回 1
print(trie.trie)
print(trie.erase("apple"))  # 移除 "apple"。现在前缀树是空的。
print(trie.trie)
print(trie.countWordsStartingWith("app"))  # 返回 0
print(trie.trie)
