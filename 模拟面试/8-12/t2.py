#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        nums = list(map(int, str(n)))
        res = [0] * len(nums)
        point = len(nums) - 1
        while point > 0:
            current = nums[point]
            if current < nums[point - 1]:
                res[point:] = [9] * (len(nums) - point)
                nums[point - 1] = nums[point - 1] - 1
            else:
                res[point] = nums[point]
            point -= 1

        if nums[0] > res[1]:
            res[0] = nums[0] - 1
            res[1:] = [9] * (len(nums) - 1)
        else:
            res[0] = nums[0]
        return int(''.join(map(str, res)))


if __name__ == '__main__':
    s = Solution()
    N = 332
    print(s.monotoneIncreasingDigits(N))
