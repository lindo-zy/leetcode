#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        while ver1 or ver2:
            x = int(ver1.pop(0)) if ver1 else 0
            y = int(ver2.pop(0)) if ver2 else 0
            if x == y:
                continue
            if x > y:
                return 1
            if x < y:
                return -1
        return 0


if __name__ == '__main__':
    sn = Solution()
    version1 = "0.1"
    version2 = "1.1"
    print(sn.compareVersion(version1, version2))
