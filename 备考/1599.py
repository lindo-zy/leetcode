#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        # 转一次runningCost
        # 乘客支付boardingCost
        # 每次尽量让4个乘客上车

        # idx, n, waiting = 0, len(customers), 0
        # min_rotates, max_profit = -1, 0  # 正数不包括 0
        # profit, cnt = 0, 1
        # while idx < n or waiting != 0:  # 循环结束条件
        #     # 1.先处理每波游客(必须的，时间顺序)
        #     if idx < n:
        #         waiting += customers[idx]
        #         idx += 1
        #     # 2.计算登基人数，等多4个人
        #     if waiting >= 4:
        #         board = 4
        #         waiting -= 4
        #     else:
        #         board = waiting
        #         waiting = 0
        #     # 3.计算利润和和更新历史最大收益时的转动次数
        #     profit += board * boardingCost - runningCost
        #     if profit > max_profit:
        #         min_rotates, max_profit = cnt, profit
        #     cnt += 1  # 转动次数累加
        # return min_rotates

        waiting = 0
        res, max_profit = -1, 0  # 正数不包括 0
        profit, rotates = 0, 1
        while customers or waiting > 0:  # 循环结束条件

            waiting += customers.pop(0) if customers else 0  # 这一轮的等待人数
            board = min(4, waiting)  # 这一轮的登舱人数
            waiting = max(0, waiting - 4)  # 这一轮登舱后的等待人数
            profit += board * boardingCost - runningCost  # 当前总收益，这一轮的边际收益=人数*单价-成本

            if profit > max_profit:  # 边际收益大于零，这一轮值的运营
                res, max_profit = rotates, profit  # 更新总的圈数，总的收益
            rotates += 1  # 转动次数累加

        return res


if __name__ == '__main__':
    s = Solution()
    # customers = [8, 3]
    # boardingCost = 5
    # runningCost = 6

    # customers = [3, 4, 0, 5, 1]
    # boardingCost = 1
    # runningCost = 92

    customers = [10, 10, 6, 4, 7]
    boardingCost = 3
    runningCost = 8

    customers = [0, 43, 37, 9, 23, 35, 18, 7, 45, 3, 8, 24, 1, 6, 37, 2, 38, 15, 1, 14, 39, 27, 4, 25, 27, 33, 43, 8,
                 44, 30, 38, 40, 20, 5, 17, 27, 43, 11, 6, 2, 30, 49, 30, 25, 32, 3, 18, 23, 45, 43, 30, 14, 41, 17, 42,
                 42, 44, 38, 18, 26, 32, 48, 37, 5, 37, 21, 2, 9, 48, 48, 40, 45, 25, 30, 49, 41, 4, 48, 40, 29, 23, 17,
                 7, 5, 44, 23, 43, 9, 35, 26, 44, 3, 26, 16, 31, 11, 9, 4, 28, 49, 43, 39, 9, 39, 37, 7, 6, 7, 16, 1,
                 30, 2, 4, 43, 23, 16, 39, 5, 30, 23, 39, 29, 31, 26, 35, 15, 5, 11, 45, 44, 45, 43, 4, 24, 40, 7, 36,
                 10, 10, 18, 6, 20, 13, 11, 20, 3, 32, 49, 34, 41, 13, 11, 3, 13, 0, 13, 44, 48, 43, 23, 12, 23, 2]
    boardingCost = 43
    runningCost = 54
    print(s.minOperationsMaxProfit(customers, boardingCost, runningCost))
