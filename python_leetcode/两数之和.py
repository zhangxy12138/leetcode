# -*-coding:utf-8-*-


def twoSum(self, nums, target):
    """
    给定一个整数数组 nums和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍
    """
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                break
            if nums[i] + nums[j] == target:
                return i, j


#  二

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    sorted_id = sorted(range(len(nums)), key=lambda k: nums[k])
    head = 0
    tail = len(nums) - 1
    sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
    while sum_result != target:
        if sum_result > target:
            tail -= 1
        elif sum_result < target:
            head += 1
        sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
    return [sorted_id[head], sorted_id[tail]]


# 三：

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashmap = {}
    for index, num in enumerate(nums):
        another_num = target - num
        if another_num in hashmap:
            return [hashmap[another_num], index]
        hashmap[num] = index
    return None

# 四：
def twoSum(self, nums: List[int], target: int) -> List[int]:
    return (d := {}) or next(([d[num], i] for i, num in enumerate(nums) if num in d or d.setdefault(target - num, i) < 0))

