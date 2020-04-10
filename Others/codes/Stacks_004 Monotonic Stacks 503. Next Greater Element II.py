# Used the idea of stacks as monotonic queues

# Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.
#
# Example 1:
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number;
# The second 1's next greater number needs to search circularly, which is also 2.
# Note: The length of given array won't exceed 10000.

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) == 0:
            return []

        hashTableNGE = {}
        stack = [(nums[0], 0)]

        # for each element after nums2[0], if the next element is > top of stack, assign NGE, else push the element on stack
        # the stack represents strictly decreasing numbers. When we get a violation, means we found NGE for at least one element on top of stack
        # however, we will test it for other elemrnts of the stack till thhe stack is empty
        # Treat the orignal array as if expnded and copied over once for simulating cylicity
        for j in range(1, 2*len(nums)-1):
            if j >= len(nums):
                i = j%len(nums)
            else:
                i = j

            elm = nums[i]

            if elm <= (stack[-1][0]):
                # push the elm and the index of the expanded array
                stack.append((elm, j))
            else:
                while stack and elm > stack[-1][0]:
                    hashTableNGE[stack.pop()[1]] = elm
                stack.append((elm, j))

        while stack:
            hashTableNGE[stack.pop()[1]] = -1

        for i in range(len(nums)):
            nums[i] = hashTableNGE[i]
        return nums

obj = Solution()
# print obj.nextGreaterElements([10,5,7,3,2,6,5,1,2])
print obj.nextGreaterElements([1,2,1])