#!/usr/bin/python3
# -*- coding:utf-8 -*-

from collections import defaultdict


class Solution:
    def __init__(self, n):
        # 最大数量
        self.n = n
        # 记录生成规则
        self.record = defaultdict()
        # 维护当前的总token数
        self.total = 0
        self.time_map = defaultdict(list)
        self.time_record = defaultdict(int)

    def add_rule(self, rule_id, time, interval, num):
        # 更新存量规则
        self.check_time(time)
        if rule_id not in self.record:
            self.record[rule_id] = (time, interval, num)
            # 添加后，立即生成token添加到系统，
            if self.total + num >= self.n:
                self.total = self.n
            else:
                self.total += num
            # 当前时刻点已经生成过,后续这个时刻点就不生成了
            # 难点在于要知道哪些时刻点是满足生成规则的，记录所有时刻点,满足的时刻点记为1
            time_stamp = []
            for i in range(101):
                time_stamp.append(self.gen_rule(time, interval, i))
            self.time_map[rule_id] = time_stamp
            self.time_record[rule_id] = time
            return True
        return False

    def remove_rule(self, rule_id, time):
        # 更新存量规则
        self.check_time(time)
        if rule_id not in self.record:
            return False
        self.record.pop(rule_id)
        return True

    def trans(self, time, size):
        # 更新存量规则
        self.check_time(time)
        if self.total >= size:
            self.total -= size
            return True
        return False

    def query(self, time):
        # 更新存量规则
        self.check_time(time)
        return self.total

    def gen_rule(self, start_time, interval, n):
        # 生成规则,时间
        return n * interval + start_time

    def check_time(self, cur_time):
        # 检查全部规则，看是否满足
        for k in self.record.keys():
            time, interval, num = self.record[k]
            # 从最新的时刻点生成到cur_time
            cnt = 0
            for i in range(self.time_record[k] + 1, cur_time + 1):
                if i in self.time_map[k]:
                    cnt += 1
            self.total += cnt * num
            self.time_record[k] = cur_time
        # # 当前total的值
        if self.total >= self.n:
            self.total = self.n


if __name__ == '__main__':
    s = Solution(10)
    # 时间是跳跃，递增的
    print(s.add_rule(0, 0, 1, 1))
    print(s.total)
    print(s.add_rule(1, 2, 1, 1))
    print(s.total)
    print(s.add_rule(2, 4, 1, 1))
    print(s.total)
    print(s.remove_rule(1, 6))
    print('remo', s.total)

    # print(s.add_rule(3, 6, 1, 1))
    # print(s.total)
    print(s.add_rule(4, 7, 3, 3))
    print(s.total)

    print(s.trans(8, 10))
    print(s.total)
    # 加入不进去，但是在9这个时刻点，要更新其余的规则
    # print(s.add_rule(4, 9, 3, 3))  # 31
    # print(s.total)
    print(s.query(10))
