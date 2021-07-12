#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import deque
from typing import List


class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        right = 0
        cur = deque()
        cur.extend(nums[right:right + k])
        ans = [len(cur)]
        while right + k < n:
            # 弹出左边元素
            cur.popleft()
            cnt = len(set(cur))
            temp = nums[right + k]
            print(temp, cur)
            if temp not in cur:
                cnt += 1
            ans.append(cnt)
            cur.append(temp)
            right += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 2, 2, 1, 3]
    k = 3
    print(s.distinctNumbers(nums, k))
