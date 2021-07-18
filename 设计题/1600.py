#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import defaultdict


class ThroneInheritance:
    def __init__(self, kingName):
        self.hash = defaultdict(list)
        self.king = kingName
        self.dead = set()

    def birth(self, parentName, childName):
        self.hash[parentName].append(childName)

    def death(self, name):
        self.dead.add(name)

    def getInheritanceOrder(self):
        res = list()

        def preOrder(root):
            if root not in self.dead:
                res.append(root)
            if root in self.hash:
                for child in self.hash[root]:
                    preOrder(child)

        preOrder(self.king)
        return res


t = ThroneInheritance("king")  # 继承顺序：king
t.birth("king", "andy")  # 继承顺序：king > andy
t.birth("king", "bob")  # 继承顺序：king > andy > bob
t.birth("king", "catherine")  # 继承顺序：king > andy > bob > catherine
t.birth("andy", "matthew")  # 继承顺序：king > andy > matthew > bob > catherine
t.birth("bob", "alex")  # 继承顺序：king > andy > matthew > bob > alex > catherine
t.birth("bob", "asha")  # 继承顺序：king > andy > matthew > bob > alex > asha > catherine

t.getInheritanceOrder()  # 返回 ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
t.death("bob")  # 继承顺序：king > andy > matthew > bob（已经去世）> alex > asha > catherine
t.getInheritanceOrder()  # 返回 ["king", "andy", "matthew", "alex", "asha", "catherine"]
