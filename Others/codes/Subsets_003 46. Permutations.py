# # Learning
# Struggled a lot intermediary steps of adding element to list etc because the order of pop and insert need to be bvery specific. [Whiteboard helps a lot]
# When confused too much about something, writing detailed steps on the whiteboard helps
# Here very nice specific logic helped which was for each for loop at every stage, pop the last element then insert back on the first position and then pop the other elements...



# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#     [1,2,3],
#     [1,3,2],
#     [2,1,3],
#     [2,3,1],
#     [3,1,2],
#     [3,2,1]
# ]


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        self.allPerms = []
        self.allPaths(nums, [])
        return self.allPerms

    def allPaths(self, itemsAvl, perm):

        # Debug
        yo1 = itemsAvl
        yo2 = perm


        # Base Case (last elem left) | Note that here, we do not need to create a new list as the number left will simply go to the one perm being navigated
        if len(itemsAvl) == 1:
            perm.append(itemsAvl[0])
            self.allPerms.append(perm)
            return

        lenListItemsAvl = len(itemsAvl)
        for i in range(lenListItemsAvl):
            popElm = itemsAvl.pop()
            newDerivedPerm = list(perm)
            newDerivedPerm.append(popElm)
            self.allPaths(itemsAvl, newDerivedPerm)
            itemsAvl.insert(0, popElm)

obj = Solution()
print obj.permute([1,2,3])
print obj.permute([1])
print obj.permute([1,2])
print obj.permute([])