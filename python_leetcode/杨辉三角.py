# -*-coding:utf-8-*-

# 给定一个非负整数numRows，生成杨辉三角的前numRows行。
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

# def generate(numRows):
#     """
#     :type numRows: int
#     :rtype: List[List[int]]
#     """
#     if numRows == 1:
#         return [[1]]
#     elif numRows == 2:
#         return [[1],[1,1]]
#     else:
#         first_reslt = [[1],[1,1]]
#         for j in range(2,numRows):
#             line_reslt = [0]*(j+1)
#             line_reslt[0] = 1
#             line_reslt[j] = 1
#             for i in range(1,j):
#                 # print(j)
#                 # print(i)
#                 # print(first_reslt[j-1][i-1])
#                 # print(first_reslt[j-1][i])
#                 line_reslt[i] = first_reslt[j-1][i-1]+first_reslt[j-1][i]
#             first_reslt.append(line_reslt)
#     return first_reslt



if __name__ == '__main__':
    generate(3)
    # line = [0]*5
    # line[4] =1
    # print(line)