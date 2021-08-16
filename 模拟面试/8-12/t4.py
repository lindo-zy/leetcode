#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import Counter
from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # 映射字母对应的分数
        def get_score(le_count):
            return sum([score[ord(l) - ord('a')] * num for l, num in le_count.items()])

        length = len(words)
        letter_count = Counter(letters)
        total_count = get_score(letter_count)

        self.ans = 0

        def dfs(count, start):
            if start >= length:
                self.ans = max(self.ans, total_count - get_score(count))
                return
            if not (Counter(words[start]) - count):
                dfs(count - Counter(words[start]), start + 1)
            dfs(count, start + 1)

        dfs(letter_count, 0)

        return self.ans


if __name__ == '__main__':
    s = Solution()
    words = ["dog", "cat", "dad", "good"]
    letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
    score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(s.maxScoreWords(words, letters, score))
