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



------



