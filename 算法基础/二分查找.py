#!/usr/bin/python3
# -*- coding:utf-8 -*-


def binary_search(arr, val):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < val:
            low = mid + 1
        else:
            high = mid
    return low


arr = list(range(10))
print(arr)
print(binary_search(arr, 7))
