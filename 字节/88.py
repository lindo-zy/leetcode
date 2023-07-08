#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1的长度为m+n
        k = m + n - 1
        while m and n:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[k] = nums1[m - 1]
                m -= 1
            else:
                nums1[k] = nums2[n - 1]
                n -= 1
            k -= 1
        # 处理剩下未合并的
        nums1[:n] = nums2[:n]
        print(nums1)


if __name__ == '__main__':
    sn = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(sn.merge(nums1, m, nums2, n))
