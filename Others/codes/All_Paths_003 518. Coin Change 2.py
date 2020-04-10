# Try
# To prevent from having different permutations which will be called as duplicates here, try using the subset methodology of generating different subsets, which similar to this expects different permutations as one subset.
# to do that, if coins are 1,2,3 .... allow 11111..., 111112222.., 111122223333, 22222.., 222223333..., 33333..
# this will prevent dupes like 21111... (which will already be covered in 111122222... (same as sorting in the subset problem)
# The abbove works but DP doesnt work with soln as DP does not know what coins were used to create a prev calculated sum, and hence 2111 type of pattern has no way to be checked

# https://www.youtube.com/watch?v=sn0DWI-JdNA
# Gayle's soln - make change for 3 using 1,2
# we can use 0 1s, 1 1s, 2 1s, 3 1s.., 0 2s, 1 2s...

# Back to Back SWE
# https://www.youtube.com/watch?v=DJ4a7cmjZY0&t=538s

# You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
#
#
#
# Example 1:
#
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# Example 2:
#
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# Example 3:
#
# Input: amount = 10, coins = [10]
# Output: 1
#
#
# Note:
#
# You can assume that
#
# 0 <= amount <= 5000
# 1 <= coin <= 5000
# the number of coins is less than 500
# the answer is guaranteed to fit into signed 32-bit integer


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        self.coins = coins
        # self.coins.sort()
        self.MEM = {}
        # return self.numPathsToN(amount, 0)
        return self.makeChange(coins, amount, 0)
        # return self.count(coins, len(coins), amount)

    # def count(self, S, m, n):
    #
    #     # If n is 0 then there is 1
    #     # solution (do not include any coin)
    #     if (n == 0):
    #         return 1
    #
    #     # If n is less than 0 then no
    #     # solution exists
    #     if (n < 0):
    #         return 0;
    #
    #         # If there are no coins and n
    #     # is greater than 0, then no
    #     # solution exist
    #     if (m <=0 and n >= 1):
    #         return 0
    #
    #     # count is sum of solutions (i)
    #     # including S[m-1] (ii) excluding S[m-1]
    #     return self.count( S, m - 1, n ) + self.count( S, m, n-S[m-1] );

    def numPathsToN(self, n, lastCoin):

        # if n in self.MEM:
        #     return self.MEM[n]

        if n == 0:
            return 1
        elif n < 0:
            return 0

        numTotal = 0
        for coin in self.coins:
            if coin >= lastCoin:
                numTotal += self.numPathsToN(n-coin, coin)

        # self.MEM[n] = numTotal
        return numTotal

    # Gayle's soln
    def makeChange(self, coins, money, index):

        # print str(money) + '-' + str(index)

        if money == 0:
            return 1
        if index >= len(coins):
            return 0

        key = str(money) + '-' + str(index)
        if key in self.MEM:
            return self.MEM[key]

        amountWithCoin = 0
        ways = 0
        while amountWithCoin <= money:
            remaining = money - amountWithCoin
            ways += self.makeChange(coins, remaining, index + 1)
            amountWithCoin += coins[index]
        self.MEM[key] = ways
        return ways

    # Leetcode answer (should be same as Back to Back SWE)
class Solution:
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]

obj = Solution()
print obj.change(amount = 5, coins = [1, 2, 5])
print obj.change(amount = 5, coins = [5,1,2])
print obj.change(amount = 3, coins = [2, 1])