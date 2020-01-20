#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m + n] = nums2
        nums1.sort()
