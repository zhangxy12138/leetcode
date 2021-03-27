# -*-coding:utf-8-*-

# 给出由小写字母组成的字符串S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
# 
# 在 S 上反复执行重复项删除操作，直到无法继续删除。
# 
# 在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
#
# 示例：
# 
# 输入："abbaca"
# 输出："ca"
# 解释：
# 例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
# 
# 
# 提示：
# 
# 1 <= S.length <= 20000
# S 仅由小写英文字母组成

'''
题解：栈
'''



# def removeDuplicates(S):
#     """
#     :type S: str
#     :rtype: str
#     """
#     stack = []
#     for i in S:
#         print(stack)
#         if stack and i == stack[-1]:  # stack不为空，且字符串第一个等于栈顶；
#             stack.pop()
#         else:
#             stack.append(i)
#     return "".join(stack)  # 列表变字符串

def removeDuplicates(self, S):
    """
    :type S: str
    :rtype: str
    """
    stack = [""]
    for ch in S:
        if ch == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)



if __name__ =='__main__':
    print(removeDuplicates('abbbbbca'))




