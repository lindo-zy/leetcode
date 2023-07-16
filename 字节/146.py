#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.record = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.record:
            self.record.move_to_end(key)
        return self.record.get(key, -1)

    def put(self, key: int, value: int) -> None:
        # 如果key在字典中，先弹出，避免更新的时候，位置不变
        if key in self.record:
            self.record.pop(key)
        self.record[key] = value
        if len(self.record) > self.capacity:
            self.record.popitem(last=False)
