# Problem Solving, Arrays
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
#
# Example:
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    prev_num = 1
    prev_ind_val = 1
    out = [1]*len(nums)

    for i in range(len(nums)):
        out[i] = prev_num * prev_ind_val
        prev_num = nums[i]
        prev_ind_val = out[i]

    prev_num = 1
    for i in range(len(nums)):
        neg_i = len(nums) - i - 1
        out[neg_i] = out[neg_i] * prev_num
        prev_num = nums[neg_i] * prev_num

    return out

print productExceptSelf([1,2,3,4])