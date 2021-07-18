#!/usr/bin/python3
# -*- coding:utf-8 -*-
A = [6, 0, 8, 2, 1, 5]
ans = 0
m = float('inf')

for i in sorted(range(len(A)), key=A.__getitem__):
    ans = max(ans, i - m)
    m = min(m, i)
