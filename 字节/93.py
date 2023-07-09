#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def dfs(cnt, ip, s):
            # 结束条件
            if cnt == 4:
                if s == '':
                    res.append(ip[:-1])
                return
            if len(s) > 0:
                dfs(cnt + 1, ip + s[:1] + '.', s[1:])
            if len(s) > 1 and s[0] != 0:
                dfs(cnt + 1, ip + s[:2] + '.', s[2:])
            if len(s) > 2 and s[0] != 0 and int(s[:3]) < 256:
                dfs(cnt + 1, ip + s[:3] + '.', s[3:])

        dfs(0, '', s)

        return res


if __name__ == '__main__':
    sn = Solution()
    s = "25525511135"
    print(sn.restoreIpAddresses(s))
