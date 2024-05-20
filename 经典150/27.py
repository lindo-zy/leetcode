from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        for i in range(len(nums)):
            if val ^ nums[i]:
                nums[a] = nums[i]
                a += 1
        print(nums)
        return a


if __name__ == '__main__':
    sn = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    print(sn.removeElement(nums, val))  # nums = [2,2,_,_]
