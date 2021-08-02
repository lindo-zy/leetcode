#!/usr/bin/python3
# -*- coding:utf-8 -*-


def binarySearch(nums, target):
    # 左闭右开
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
