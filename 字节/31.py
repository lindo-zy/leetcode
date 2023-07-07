#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2

        # 2, 6, 3, 5, 4, 1  ->下一个就是2, 6, 4, 1, 3, 5
        # 从后往前找，找到第一个不满足升序的数，即为3
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # 说明已经是最大了，下一个数反转即可
        if i < 0:
            nums.reverse()
            return

        # 找到第一个比nums[i]大的数,即为4
        j = n - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        # 交换3和4，得到 2, 6, 4, 5, 3, 1
        nums[i], nums[j] = nums[j], nums[i]

        # 即反转nums[i+1:],使得生产的序列最小，531反转后即为135最小
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        # 2, 6, 4, 1, 3, 5
        print(nums)


if __name__ == '__main__':
    sn = Solution()
    nums = [2, 6, 3, 5, 4, 1]
    print(sn.nextPermutation(nums))
