#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import defaultdict, Counter
from typing import List


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        def atMost(k, nums):
            i = ans = 0
            win = defaultdict(lambda: 0)
            for j in range(len(nums)):
                if win[nums[j]] == 0:
                    k -= 1
                win[nums[j]] += 1
                while k < 0:
                    win[nums[i]] -= 1
                    if win[nums[i]] == 0:
                        k += 1
                    i += 1
                ans = max(ans, j - i + 1)
            return ans

        return atMost(2, tree)

    def totalFruit2(self, tree: List[int]) -> int:
        n = len(tree)
        seen = Counter()
        l = 0
        r = 0
        res = 0
        while r < n:
            if len(seen) == 2 and tree[r] not in seen:
                res = max(res, r - l)
                for t in seen:
                    if t != tree[r - 1]:
                        break
                l = seen[t] + 1
                seen.pop(t)
            seen[tree[r]] = r
            r += 1
        return max(res, r - l)


if __name__ == '__main__':
    s = Solution()
    tree = [1, 2, 3, 2, 2]  # 4
    print(s.totalFruit(tree))
    print(s.totalFruit2(tree))
