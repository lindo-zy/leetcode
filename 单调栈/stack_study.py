#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic, stack = {}, []

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                dic[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        return [dic.get(x, -1) for x in nums1]

    def func(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                res[idx] = nums[i]
            stack.append(i)
        return res


class Solution2:
    def nextGreaterElement(self, n: int) -> int:
        INF = 1 << 32 - 1
        n = list(str(n))
        stack = []
        for i in range(len(n) - 1, -1, -1):
            j = -1
            while stack and n[stack[-1]] > n[i]:  # 单调递增栈
                j = stack.pop()
            if j >= 0:
                tmp = n[i]
                n[i] = n[j]
                n[j] = tmp

                n = n[:i + 1] + sorted(n[i + 1:])  # 重排后面的值
                n = int(''.join(n))
                return n if n <= INF else -1
            stack.append(i)
        return -1


class Solution3:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums = nums * 2
        stack = []
        res = [-1] * len(nums)
        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
            stack.append(idx)

        return res[:len(nums) // 2]


class Solution4:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = []  # 存储元素序号
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                ans[stack.pop()] = i - stack[-1]

            stack.append(i)
        return ans


class Solution5:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        while left <= right and nums[left] == sort_nums[left]:
            left += 1
        while left <= right and nums[right] == sort_nums[right]:
            right -= 1
        return right - left + 1


class Solution6:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for e in tokens:
            if e in '+-*/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(str(int(eval(num2 + e + num1))))
            else:
                stack.append(e)
        return int(stack[0])


if __name__ == '__main__':
    # sn = Solution()
    # nums1 = [4, 1, 2]
    # nums2 = [1, 3, 4, 2]
    # print(sn.nextGreaterElement(nums1, nums2))

    sn2 = Solution2()
    # n = 12  # 21
    # n = 21  # -1
    # n = 1081  # -1
    # print(sn2.nextGreaterElement(n))

    sn3 = Solution3()
    # n = [1, 2, 1]  # [2,-1,2]
    # print(sn3.nextGreaterElements(n))
    #
    # sn4 = Solution4()
    # temperatures = [73, 74, 75, 71, 69, 72, 76, 73]  # [1, 1, 4, 2, 1, 1, 0, 0]
    # print(sn4.dailyTemperatures(temperatures))

    sn5 = Solution5()
    # n = [2, 6, 4, 8, 10, 9, 15]  # [6, 4, 8, 10, 9]
    # # n = [1, 2, 3, 4]  # 0
    # print(sn5.findUnsortedSubarray(n))

    sn6 = Solution6()
    t = ["2", "1", "+", "3", "*"]  # 9
    # t = ["4", "13", "5", "/", "+"]  # 6
    print(sn6.evalRPN(t))
