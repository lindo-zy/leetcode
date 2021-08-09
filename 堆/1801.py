# -*- coding:utf-8 -*-
import heapq
from typing import List


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy, sell = [], []

        for price, amount, order_type in orders:
            if order_type == 0:
                match_price = sell and sell[0][0]
                while amount > 0 and sell and sell[0][0] <= price:
                    match_price, delta = heapq.heappop(sell)
                    amount -= delta
                if amount < 0:
                    heapq.heappush(sell, (match_price, -amount))
                if amount > 0:
                    heapq.heappush(buy, (-price, amount))
            else:
                match_price = buy and -buy[0][0]
                while amount > 0 and buy and -buy[0][0] >= price:
                    match_price, delta = heapq.heappop(buy)
                    amount -= delta
                if amount < 0:
                    heapq.heappush(buy, (match_price, -amount))
                if amount > 0:
                    heapq.heappush(sell, (price, amount))
        return (sum(list(map(lambda x: x[1], buy))) + sum(list(map(lambda x: x[1], sell)))) % (10 ** 9 + 7)


if __name__ == '__main__':
    s = Solution()
    orders = [[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]
    print(s.getNumberOfBacklogOrders(orders))
