# -*-coding:utf-8-*-

# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例1:
#
# 输入: 123
# 输出: 321
# 示例 2:
# 输入: -123
# 输出: -321
# 示例 3:
# 输入: 120
# 输出: 21
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为[−231, 231− 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

# 一：
x = 10
def reverse(x):
    i = 1
    j = 1
    if x <0:
        fuhao = False
    else:
        fuhao = True

    x = abs(x)
    y = 0
    while x/i >= 10:
        i = i*10
    while x > 0:
        y = (x // i) * j + y
        x = x-(x//i)*i
        j = j*10
        i = i//10
    if fuhao == False:
        y = y*(-1)
    if (y< (-2**31) )or (y >(2**31)-1):
        return 0
    else:
        return y

# 二
def reverse(self, x: int) -> int:
    max_integer = 2 ** 31 - 1
    min_integer = - 2 ** 31
    sign = 1 if x >= 0 else -1
    x = abs(x)
    reverse = 0

    while x > 0:
        reverse = reverse * 10 + x % 10
        x = x // 10

    res = sign * reverse
    return res if res >= min_integer and res <= max_integer else 0

# 三
def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    if x==0:
        return 0
    str_x = str(x)
    x = ''
    if str_x[0] == '-':
        x += '-'
    x += str_x[len(str_x)-1::-1].lstrip("0").rstrip("-")
    x = int(x)
    if -2**31<x<2**31-1:
        return x
    return 0

# lstrip() 方法用于截掉字符串左边的空格或指定字符
# rstrip() 删除 string 字符串末尾的指定字符（默认为空格）
# str_x[len(str_x)-1::-1] = 01-


# 四：
def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """

    b = str(x).split('-')  # 把数字转字符串并对-分割，如果有- 则列表长度为2
    if len(b) > 1:
        n = (int('-' + b[1][::-1]))  # 把下标1的字符串反转再加上- 并转int
        if -2 ** 31 < n < 2 ** 31 - 1:
            return n
        else:
            return 0
    else:
        n = (int(b[0][::-1]))
        if -2 ** 31 < n < 2 ** 31 - 1:
            return n
        else:
            return 0


# 五：
# int reverse(int x)
# {
# 	long n = 0;
# 	while (x)
# 	{
# 		n = n * 10 + x % 10;
# 		x /= 10;
# 	}
# 	return n > INT_MAX || n < INT_MIN ? 0 : n;
# }

