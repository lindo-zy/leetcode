#!/usr/bin/python3
# -*- coding:utf-8 -*-
import random
import time


class Solution:
    def twoSum(self, nums, target):
        ds = dict(zip(nums, [i for i in range(len(nums))]))
        print(ds)
        for index, n in enumerate(nums):
            temp = target - n
            print(temp)
            if temp in ds and ds[temp] != index:
                return sorted([ds[temp], index])
        return None

# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None


if __name__ == '__main__':
    start = time.time()
    print(start)
    s = Solution()
    ls = []
    # for i in range(10):
    #     ls.append(random.randint(0, 100))
    nums = [3, 2, 4]
    # target = random.randint(0, 100)
    target = 6
    print(target)
    result = s.twoSum(nums, target)
    print(result)
    print(time.time())
