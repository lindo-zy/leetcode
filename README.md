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





题目描述：[有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)

```
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



代码：

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Solution:
    def isValid(self, s: str) -> bool:
        while '{}' in s or '[]' in s or '()' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ""


if __name__ == '__main__':
    sn = Solution()
    s = '([)]'
    s = '{[]}'
    # s = '(]'
    # s = '[])'
    result = sn.isValid(s)
    print(result)

```

思路：

```

```







题目描述：[合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

```
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



代码：

```python

```

思路：

```

```







题目描述：[删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)

```
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2], 

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。
说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



代码：

```python
class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        for num in nums:
            if nums[i] != num:
                i += 1
                nums[i] = num
        return i + 1


if __name__ == '__main__':
    s = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # nums = [1, 2]
    result = s.removeDuplicates(nums)
    print(result)
    
```

思路：

```

```







题目描述：[移除元素](https://leetcode-cn.com/problems/remove-element/)

```
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:

给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



代码：

```python
class Solution:
    def removeElement(self, nums, val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)



if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 2, 3]
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    nums = [3]
    val = 2
    result = s.removeElement(nums, val)
    print(result)
```

思路：

```

```





题目描述：[实现 strStr()](https://leetcode-cn.com/problems/implement-strstr/)

```
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



代码：

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
            try:
                return haystack.index(needle)
            except Exception:
                return -1
```

思路：

```

```







题目描述：[搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/)

```
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



代码：

```python
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            return sorted(nums).index(target)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    target = 2
    result = s.searchInsert(nums, target)
    print(result)
```

思路：

```

```





题目描述：[外观数列](https://leetcode-cn.com/problems/count-and-say/)

```
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。

注意：整数序列中的每一项将表示为一个字符串。

 

示例 1:

输入: 1
输出: "1"
示例 2:

输入: 4
输出: "1211"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-and-say
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



代码：

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.bs(self.countAndSay(n - 1))

    def bs(self, string):
        lis = list(string)
        lis.append('0')  # 末尾补一个，方便后续计数
        lis1 = []
        re = 0
        i = 0
        while i < len(lis) - 1:
            if lis[i] != lis[i + 1]:
                lis1.append(str(i + 1 - re))  # 当前计录的值的个数
                lis1.append(lis[i])  # 当前记录的值
                re = i + 1
            i = i + 1
        s = ''.join(lis1)  # 列表转字符串
        return s

```

思路：

```

```







题目描述：[最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)

```
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



代码：

```python
class Solution:
    def maxSubArray(self, nums) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i - 1], 0)
        return max(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [-1,-2,-3]
    # [4, -1, 2, 1]
    result = s.maxSubArray(nums)
    print(result)
```

思路：

```

```







题目描述：[最后一个单词的长度](https://leetcode-cn.com/problems/length-of-last-word/)

```
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"
输出: 5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/length-of-last-word
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



代码：

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(' ')  # 去掉末尾空格
        L = s.split(' ')[-1]  
        return len(L)


if __name__ == '__main__':
    s = Solution()
    string = 'Hello World'  # 5
    # string = ''  # 0
    string = 'a'  # 1
    result = s.lengthOfLastWord(string)
    print(result)
```

思路：

```

```





题目描述：[加一](https://leetcode-cn.com/problems/plus-one/)

```
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



代码：

```python
class Solution:
    def plusOne(self, digits):
        return list(map(int, str(int(''.join([str(i) for i in digits])) + 1)))


if __name__ == '__main__':
    s = Solution()
    digits = [1, 2, 3]  # [1,2,4]
    digits = [4, 3, 2, 1]  # [4,3,2,2]
    # digits = [0]  # [1]
    # digits = [9, 9, 9]  # [1,0,0,0]
    result = s.plusOne(digits)
    print(result)

```

思路：

```

```





题目描述：[二进制求和](https://leetcode-cn.com/problems/add-binary/)

```
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



代码：

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        r, p = '', 0
        d = len(b) - len(a)
        a = '0' * d + a
        b = '0' * -d + b
        for i, j in zip(a[::-1], b[::-1]):
            s = int(i) + int(j) + p
            r = str(s % 2) + r
            p = s // 2

        return '1' + r if p else r


if __name__ == '__main__':
    s = Solution2()
    a = '11'
    b = '1'  # 01
    a = '1010'
    b = '1011'
    result = s.addBinary(a, b)
    print(result)  # 100 10101


```

思路：

```

```



------



