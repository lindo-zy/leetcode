#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        # 钥匙记录
        visited = {0}

        def dfs(room_index, visited):
            visited.add(room_index)
            for key in rooms[room_index]:
                if key not in visited:
                    dfs(key, visited)

        dfs(0, visited)
        return len(visited) == len(rooms)


if __name__ == '__main__':
    s = Solution()
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    rooms = [[1], [2], [3], []]
    print(s.canVisitAllRooms(rooms))
