# LEARNINGS
# Had some problems with the function definition - KNOW WHAT THE FUNCITON IS DOING
# TOP DOWN VS BOTTOM UP DP
# https://docs.google.com/document/d/1RFMbtAgZo_ZOAj79aK8g33y3R7C0E2GXvxEP1wThxkw/edit?folder=1sSaIdBp85lxaDv6HL6_kKmQW-F6XTD9t

# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example 1:
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
#
# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.


# GREEDY WHICH DOES NOT WORK
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        self.amount = amount
        # sort coins
        coins.sort(reverse=True)

        self.coins = coins
        self.MEM_No_Solns = set()

        ret = self.addCoin(0, 0)

        if ret != None:
            return ret
        else:
            return -1



    def addCoin(self, sum, numCoins):

        # Check DP if the current sum leads to no soln
        if sum in self.MEM_No_Solns:
            return

        # Base Case - check sum
        if sum > self.amount:
            return
        # Greedy
        elif sum == self.amount:
            return numCoins

        for coin in self.coins:
            ret = self.addCoin(sum+coin, numCoins+1)

            # Greedy: Break when the first solution is found
            if ret != None:
                return ret

        # Code reaches here => no solution for the given sum. Store for DP
        self.MEM_No_Solns.add(sum)

# ECPLORE ALL PATHS - USING ToP DOWN
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        self.amount = amount
        coins.sort(reverse=True)
        self.coins = coins


        # Memory for DP: signifies the number of coins to be added further from an amount to reach the target. When an amount does not lead to a target, assign value as None
        self.MEM = {}

        ans = self.minCostFromN(0)

        return ans if ans != float('inf') else -1





    def minCostFromN(self, num):
        if num in self.MEM:
            return self.MEM[num]
        if num == self.amount:
            return 0
        elif num > self.amount:
            return float('inf')

        minCost = float('inf')
        for coin in self.coins:
            minCost = min(minCost, 1+ self.minCostFromN(num+coin))

        self.MEM[num] = minCost
        return minCost

# ECPLORE ALL PATHS - USING BOTTOM UP
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        DP_ARRAY = [float('inf')]*(amount+1)
        DP_ARRAY[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i-coin >= 0:
                    DP_ARRAY[i] = min(DP_ARRAY[i], 1+DP_ARRAY[i-coin])
        return DP_ARRAY[amount] if DP_ARRAY[amount] != float('inf') else -1


obj = Solution()
# print obj.coinChange(coins = [1, 2, 5], amount = 3)
print obj.coinChange(coins = [1, 2, 5], amount = 11)
print obj.coinChange(coins = [1], amount = 0)
print obj.coinChange(coins = [2], amount = 3)
# print 10