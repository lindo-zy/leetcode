#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class FileSystem:

    def __init__(self):
        self.tries = {}

    def gen_tree(self, path: str):
        path = [i for i in path.split('/') if i]
        cur_node = self.tries
        for c in path:
            if c not in cur_node:
                cur_node[c] = {}
            cur_node = cur_node[c]
        return [cur_node, path]

    def ls(self, path: str) -> List[str]:
        node, path = self.gen_tree(path)
        if 'content' in node:
            return [path[-1]]
        else:
            return sorted(list(node.keys()))

    def mkdir(self, path: str) -> None:
        self.gen_tree(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node, path = self.gen_tree(filePath)
        if 'content' not in node:
            node['content'] = content
        else:
            node['content'] += content

    def readContentFromFile(self, filePath: str) -> str:
        node, path = self.gen_tree(filePath)
        return node['content']


fs = FileSystem()
fs.ls('/')  # []
fs.mkdir('/a/b/c')  # null
fs.addContentToFile('/a/b/c/d', 'hello')  # null
print(fs.ls('/'))  # ['a']
print(fs.readContentFromFile('/a/b/c/d'))  # hello
