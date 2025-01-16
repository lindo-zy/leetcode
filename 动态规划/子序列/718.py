# 给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的子数组的长度 。
#
#
#
#  示例 1：
#
#
# 输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# 输出：3
# 解释：长度最长的公共子数组是 [3,2,1] 。
#
#
#  示例 2：
#
#
# 输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# 输出：5
#
#
#
#
#  提示：
#
#
#  1 <= nums1.length, nums2.length <= 1000
#  0 <= nums1[i], nums2[i] <= 100
#
#
#  Related Topics 数组 二分查找 动态规划 滑动窗口 哈希函数 滚动哈希 👍 1145 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        if n < m:
            n, m = m, n
        # 长度为i的最长公共子数组
        dp = [0] * (m + 1)
        ans = 0
        for i in range(1, n + 1):
            for j in range(m, 0, -1):
                # 子数组要求连续
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = dp[j - 1] + 1
                else:
                    dp[j] = 0
                ans = max(ans, dp[j])
        return ans


# leetcode submit region end(Prohibit modification and deletion)

sol = Solution()
print(sol.findLength(nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4, 7]))
