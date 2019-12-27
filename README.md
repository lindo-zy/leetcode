# 使用python刷leetcode

### 简单



题目描述：两数之和

```
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



代码：

```python
import random


class Solution:
    def twoSum(self, nums, target):
        ds = dict(zip(nums, [i for i in range(len(nums))]))
        print(ds)
        for index, n in enumerate(nums):
            temp = target - n
            print(temp)
            if temp in ds and ds[temp] != index:
                return sorted([ds[temp], index])
        return None


if __name__ == '__main__':
    s = Solution()
    ls = []
    # for i in range(10):
    #     ls.append(random.randint(0, 100))
    nums = [3, 2, 4]
    # target = random.randint(0, 100)
    target = 6
    print(target)
    result = s.twoSum(nums, target)
    print(result)
```

思路：

```

```





题目描述：整数反转

```
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



代码：

```python
class Solution:
    def reverse(self, x: int) -> int:
        x_min = -2 ** 31
        x_max = 2 ** 31 - 1

        if str(x)[0] == '-':
            result = int('-' + str(x)[1:][::-1])
        else:
            result = int(str(x)[::-1])
        if x_min <= result <= x_max:
            return result
        return 0


if __name__ == '__main__':
    s = Solution()
    x = 1534236469
    x = 123
    x = 120
    x = -120
    result = s.reverse(x)
    print(result)
```

思路：

```

```





题目描述：回文数

```
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



代码：

```python
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            temp = str(x)
            if temp == temp[::-1]:
                return True
            return False


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        div = 1
        while x / div >= 10:
            div *= 10

        while x > 0:
            left = x // div
            right = x % 10
            if left != right:
                return False
            x = (x % div) // 10
            div //= 100
        return True
```

思路：

```

```





题目描述：[罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer/)

```
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:

输入: "III"
输出: 3
示例 2:

输入: "IV"
输出: 4
示例 3:

输入: "IX"
输出: 9
示例 4:

输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
示例 5:

输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/roman-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



代码：

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        ds = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for i in range(len(s)):
            if i < len(s) - 1 and ds[s[i]] < ds[s[i + 1]]:
                num -= ds[s[i]]
            else:
                num += ds[s[i]]

        if 1 <= num <= 3999:
            return num


if __name__ == '__main__':
    sn = Solution()
    s = 'LVIII'  # 58 L=50 V=5 III=3
    s = 'MCMXCIV'  # 1994 M=1000 CM=900 XC=90 IV=4
    # s = 'MMMCMXCIX'  # 3999 MMMCMXCIX 3000=MMM CM=900 XC=90 IC=9
    result = sn.romanToInt(s)
    print(result)
```

思路：

```

```





题目描述：[最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix/)

```
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



代码：

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        s1 = min(strs)
        s2 = max(strs)

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return s2[:i]
        return s1

class Solution2:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        ss = list(map(set, zip(*strs)))
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res


if __name__ == '__main__':
    s = Solution()
    strs = ["dog", "racecar", "car"]
    strs = ["flower", "flow", "flight"]
    result = s.longestCommonPrefix(strs)
    print(result)

```

思路：

```

```



------



