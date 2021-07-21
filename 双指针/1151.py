#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        win_len = data.count(1)
        n = len(data)
        ans = 0
        # 当前窗内1个数
        cur = data[:win_len].count(1)
        for i in range(n - win_len):
            cur += data[i + win_len] - data[i]
            ans = min(ans, win_len - cur)
        return ans

        # size = data.count(1)
        # count = data[:size].count(1)
        # ans = size-count
        # for i in range(len(data)-size):
        #     count += data[i+size] - data[i]
        #     ans = min(ans, size-count)
        # return ans


if __name__ == '__main__':
    s = Solution()
    data = [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]
    # data = [0,0,0,1,0]
    print(s.minSwaps(data))
