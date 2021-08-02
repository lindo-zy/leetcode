#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        left, right = 0, arr[-1]

        def check(mid):
            cnt = 0
            for i in arr:
                if i > mid:
                    cnt += mid
                else:
                    cnt += i
            return cnt

        while left < right:
            mid = (left + right) // 2
            if check(mid) > target:
                right = mid
            else:
                left = mid + 1
            # 理解这个地方就完事了
            if right - left < 2:
                break
        # 后处理
        # 如果差值一样，返回小的
        left_num = abs(check(left) - target)
        right_num = abs(check(right) - target)
        if left_num == right_num:
            return left
        elif left_num < right_num:
            return left
        else:
            return right


if __name__ == '__main__':
    s = Solution()
    arr = [4, 9, 3]
    target = 10

    arr = [60864, 25176, 27249, 21296, 20204]
    target = 56803  # 11361

    arr = [48772, 52931, 14253, 32289, 75263]
    target = 40876  # 8175
    print(s.findBestValue(arr, target))
