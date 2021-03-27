# -*-coding:utf-8-*-

# n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。
#
# 如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。
#
# 给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子 的最大数量

# 在同行或者同列记为有一条边
# 转化为求图的连通分量的问题；
# 剩下的石头 = 连通分量的个数；
# 可拿走的石头 = 总数-连通分量的个数；

# def removeStones(self, stones): # 报错
#     """
#     :type stones: List[List[int]]
#     :rtype: int
#     """
#     start = len(stones)
#     for i in range(len(stones)-1):
#         if stones[i][0] == stones[i+1][0]:
#             stones.pop(i+1)
#
#     for i in range(len(stones) - 1):
#         if stones[i][1] == stones[i + 1][1]:
#             stones.pop(i + 1)
#     end = start - len(stones)
#     return end
#
# stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# print(removeStones(stones))

# class UFS():
#     def __init__(self, N):
#         self.p = range(N)
#
#     def find(self, x):
#         if self.p[x] != x:
#             self.p[x] = self.find(self.p[x])
#         return self.p[x]
#
#     def union(self, x, y):
#         xr = self.find(x)
#         yr = self.find(y)
#         self.p[xr] = yr
#
#
# class Solution(object):
#     def removeStones(self, stones):
#         ufs = UFS(20000)
#         for x, y in stones:
#             ufs.union(x, y + 10000)
#         return len(stones) - len({ufs.find(x) for x, y in stones})




# stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
# for x, y in stones:
#     print(find(x))
# a = union([2,4],[1,4])
# print(a)