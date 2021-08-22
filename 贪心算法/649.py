#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        qd = deque([i for i, s in enumerate(senate) if s == 'D'])
        qr = deque([i for i, s in enumerate(senate) if s == 'R'])
        # 加到下一轮
        while qr and qd:
            if qr[0] < qd[0]:
                qd.popleft()
                qr.append(qr.popleft() + n)
            else:
                qr.popleft()
                qd.append(qd.popleft() + n)
        return 'Dire' if not qr else 'Radiant'


if __name__ == '__main__':
    s = Solution()
    senate = 'RDD'
    print(s.predictPartyVictory(senate))
