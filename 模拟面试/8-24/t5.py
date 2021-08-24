#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # d = Counter(i for i, j in zip(s1, s2) if i != j)
        # if (d['x'] + d['y']) & 1 or len(s1) != len(s2):
        #     return -1
        # return sum(divmod(d['x'], 2) + divmod(d['y'], 2))

        cnt1, cnt2 = 0, 0
        for i in range(len(s1)):
            if s1[i] == 'x' and s2[i] == 'y':
                cnt1 += 1
            elif s1[i] == 'y' and s2[i] == 'x':
                cnt2 += 1
        if (cnt1 + cnt2) % 2 != 0:
            return -1
        n1, m1 = divmod(cnt1, 2)
        n2, m2 = divmod(cnt2, 2)
        return n1 + n2 + 2 * m1


if __name__ == '__main__':
    s = Solution()
    # s1 = "xx"
    # s2 = "yy"

    s1 = "xxyyxyxyxx"
    s2 = "xyyxyxxxyx"

    print(s.minimumSwap(s1, s2))
