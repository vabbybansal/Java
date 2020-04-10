class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.nums = nums
        self.k = k

        sum = 0
        for num in nums:
            sum += num
        if sum %k != 0:
            return False
        self.miniSum = sum/k

        self.nums.sort(reverse=True)

        if self.nums[0] > self.miniSum:
            return False

        while self.nums and self.nums[0] == self.miniSum:
            self.nums.pop(0)
            self.k -= 1

        # for num in nums:
        #     if num > self.miniSum:
        #         return False

        subSetSums = [0]*self.k
        return True if self.addNumberToSets(0,subSetSums) else False

    def addNumberToSets(self, ind, subSetSums):

        if ind == len(self.nums):
            for i in range(self.k):
                if subSetSums[i] != self.miniSum:
                    return False
            return True

        # Add the index number to left set
        for i in range(self.k):
            subSetSums[i] += self.nums[ind]
            if subSetSums[i] <= self.miniSum:
                if self.addNumberToSets(ind+1, subSetSums):
                    return True
            subSetSums[i] -= self.nums[ind]

# class Solution(object):
#     def canPartitionKSubsets(self, nums, k):
#         target, rem = divmod(sum(nums), k)
#         if rem: return False
#
#         def search(groups):
#             if not nums: return True
#             v = nums.pop()
#             for i, group in enumerate(groups):
#                 if group + v <= target:
#                     groups[i] += v
#                     if search(groups):
#                         return True
#                     groups[i] -= v
#                 if not group:
#                     break
#             nums.append(v)
#             return False
#
#         nums.sort()
#         if nums[-1] > target: return False
#         while nums and nums[-1] == target:
#             nums.pop()
#             k -= 1
#
#         return search([0] * k)

obj = Solution()
# print obj.canPartitionKSubsets( nums = [4, 3, 2, 3, 5, 2], k = 4)
# print obj.canPartitionKSubsets( nums = [4,1,1,1,1,2,2,1,3], k = 4)
print obj.canPartitionKSubsets([3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3870,270], 5)