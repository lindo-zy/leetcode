#!/usr/bin/python3
# -*- coding:utf-8 -*-
# !/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List
from sortedcontainers import SortedList
import numpy as np


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sort_list = SortedList(nums1)
        sort_list.update(nums2)
        return np.median(sort_list)
