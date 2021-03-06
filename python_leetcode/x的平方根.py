# -*-coding:utf-8-*-

# 实现int sqrt(int x)函数。

# 计算并返回x的平方根，其中x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
#
# 输入: 4
# 输出: 2
# 示例 2:
#
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
#  由于返回类型是整数，小数部分将被舍去


# def mySqrt(x):
#     if x == 0 or x ==1:
#         return x
#     max = x
#     min = 0
#     while (max - min > 1):
#         m = (max + min) // 2
#         if (x / m < m):
#             max = m
#         else:
#             min = m
#     return min


def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x <= 1:
        return x
    r = x
    k = 0
    while r > x / r:
        r = (r + x / r) // 2
        k+=1
    print(k)
    return int(r)

# def mySqrt(x):   # 牛顿迭代
#     if x == 0:
#         return 0
#     c,x0 = float(x),float(x)
#     while 1:
#         xi = 0.5*(x0+c/x0)
#         if abs(x0-xi) < 1e-7:
#             break
#         x0 = xi
#     return int(x0)

if __name__ =='__main__':
    print(mySqrt(8))


