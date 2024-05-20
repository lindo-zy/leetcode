from charset_normalizer.md import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(len(nums)):
            if slow < 2 or nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
        return slow


if __name__ == '__main__':
    sn = Solution()
    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    # 7, nums = [0,0,1,1,2,3,3]
    print(sn.removeDuplicates(nums2))
