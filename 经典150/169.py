from charset_normalizer.md import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = -1
        cnt = 0
        for num in nums:
            if cnt == 0:
                res = num
                cnt += 1
            elif num == res:
                cnt += 1
            else:
                cnt -= 1
        return res


if __name__ == '__main__':
    sn = Solution()
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(sn.majorityElement(nums))  # 2
