#!/usr/bin/python3
# -*- coding:utf-8 -*-
import re


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        result = re.findall('(\d+)', word)
        cnt = 0
        nums = set()
        for i in result:
            if int(i) not in nums:
                cnt += 1
                nums.add(int(i))
        return cnt


if __name__ == '__main__':
    s = Solution()
    word = "a123bc34d8ef34"
    word = "a1b01c001"
    print(s.numDifferentIntegers(word))
