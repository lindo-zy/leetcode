#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        tree = Trie()
        for word in words:
            tree.gen_trie(word)
        print(tree.ds)
        ans = ''
        for c in words:
            if c not in tree.ds:
                ans = ''
            ans += '<b>' + tree.ds[c] + '<b>'
        print(ans)


class Trie:
    def __init__(self):
        self.ds = {}

    def gen_trie(self, word):
        cur_node = self.ds
        for c in word:
            if c not in cur_node:
                cur_node[c] = {'p_cnt': 0, 'w_cnt': 0}
            cur_node = cur_node[c]
            cur_node['p_cnt'] += 1
        cur_node['w_cnt'] += 1


if __name__ == '__main__':
    sn = Solution()
    s = "aaabbcc"
    words = ["aaa", "aab", "bc"]
    print(sn.addBoldTag(s, words))
