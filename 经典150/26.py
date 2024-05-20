from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != nums[cnt]:
                cnt += 1
                nums[cnt] = nums[i]
        print(nums)
        return cnt + 1


if __name__ == '__main__':
    sn = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(sn.removeDuplicates(nums))  # 5, nums = [0,1,2,3,4]
