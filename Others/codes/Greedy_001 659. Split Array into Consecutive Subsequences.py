# Greedy:
# here very tricky without any standard algorithm, but I went with intuition with a soln of hash maps
# the key was to identify that this algo works fine with the greedy soln

# Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.
#
#
#
# Example 1:
#
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3
# 3, 4, 5

# class Solution(object):
#
#     historyHash = {}
#     # contains virtual lists
#     # key of n means hash[n] is a list which contains all the lists which need n as en end element
#     # Example, if hash[5] = [1,2], it means we already have two lists starting with 1 and 2 - 1,2,3,4 and 2,3,4 which both need 5
#
#     def isPossible(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         self.historyHash = {}
#
#
#         for num in nums:
#             self.manageHashAdd(num)
#
#         for key in self.historyHash:
#             allLists = self.historyHash[key]
#             for aList in allLists:
#                 if key - aList < 3:
#                     return False
#         return True
#
#     def manageHashAdd(self, num):
#
#         # Case 1: element not required (not present in has)
#         if num not in self.historyHash:
#             currentList = num
#
#         # Case 2: element required (present in hash) and only one virtualList needs it
#         elif len(self.historyHash[num]) == 1:
#             currentList = self.historyHash[num][0]
#             # Remove this element from the hash (n+1) will be added later at the end of the function
#             del self.historyHash[num]
#         # Case 3: element required in multiple virtual lists and we would greedily add it to the min length list
#         else:
#             allLists = self.historyHash[num]
#             # Find the virtual list with the min length / max initial number
#             minNumMaxIndex = 0
#             for i in range(1, len(allLists)):
#                 if allLists[i] > allLists[minNumMaxIndex]:
#                     minNumMaxIndex = i
#             # Element at minNumMaxIndex represents the virtualList with the least number of elements
#             # Remove this from the 'alllists'
#             currentList = allLists[minNumMaxIndex]
#             del allLists[minNumMaxIndex]
#
#         # Add the virtual list at n+1 key of the hash
#         # If num + 1 reqd, append this new list into that, else create key for n+1
#         # n+1 not in hash
#         if num + 1 not in self.historyHash:
#             # virtualListLog = [num]
#             self.historyHash[num+1] = [currentList]
#         # n+1 present in hash
#         else:
#             self.historyHash[num+1].append(currentList)

# ABOVE IS WORKING COPY. THIS IS AN ATTEMPT TO SPEED THIS UP FURTHER

class Solution(object):

    historyHash = {}
    # contains virtual lists
    # key of n means hash[n] is a list which contains all the lists which need n as en end element
    # Example, if hash[5] = [1,2], it means we already have two lists starting with 1 and 2 - 1,2,3,4 and 2,3,4 which both need 5

    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.historyHash = {}
        self.MIN = None


        for num in nums:
            if self.MIN is not None and num > self.MIN:
                return False
            self.manageHashAdd(num)

        for key in self.historyHash:
            allLists = self.historyHash[key]
            for aList in allLists:
                if key - aList < 3:
                    return False
        return True

    def manageHashAdd(self, num):

        # Case 1: element not required (not present in has)
        if num not in self.historyHash:
            currentList = num

        # Case 2: element required (present in hash) and only one virtualList needs it
        elif len(self.historyHash[num]) == 1:
            currentList = self.historyHash[num][0]
            # Remove this element from the hash (n+1) will be added later at the end of the function
            del self.historyHash[num]
        # Case 3: element required in multiple virtual lists and we would greedily add it to the min length list
        else:
            allLists = self.historyHash[num]
            # Find the virtual list with the min length / max initial number
            minNumMaxIndex = 0
            for i in range(1, len(allLists)):
                if allLists[i] > allLists[minNumMaxIndex]:
                    minNumMaxIndex = i
            # Element at minNumMaxIndex represents the virtualList with the least number of elements
            # Remove this from the 'alllists'
            currentList = allLists[minNumMaxIndex]
            del allLists[minNumMaxIndex]


        whatIsStartingNum = currentList
        whatIsEndingNum = num
        whatIsListLen = num - currentList + 1
        if whatIsListLen < 3:
            minNumReq = num+1

        # Add the virtual list at n+1 key of the hash
        # If num + 1 reqd, append this new list into that, else create key for n+1
        # n+1 not in hash
        if num + 1 not in self.historyHash:
            # virtualListLog = [num]
            self.historyHash[num+1] = [currentList]
        # n+1 present in hash
        else:
            self.historyHash[num+1].append(currentList)




obj = Solution()
# print obj.isPossible([1,2,3,4,6,7,8])
# print obj.isPossible([1,2,3,3,4,5])
# print obj.isPossible([1,2,3,3,4,4,5,5])
# print obj.isPossible([1,2,3,4,4,5])
print obj.isPossible([4,5,6,7,7,8,8,9,10,11])


