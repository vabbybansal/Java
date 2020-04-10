# Did it via amazing technique
# Main concept to remember though is how to find the number of digits? (also useful to find the most significant digit in a number)
# number of digits in a number num = floor[log(num)/log(10)] + 1
# COME BACK:
# twos = {2,5,6,9} | ones = {0,1,8} | threes = {3,4,7}
#       f(999) = x
#       g(999, 'ones') = f(999)
#       f(1999) = f(999) + g(1, 999)
#           g(1, 999) = f(999, 'ones')
#       f(2999) = f(1999) + g(999, 2)
#           g(999, 2) = g(999, 'twos') = f(2999) - f(1999)
#       f(3999) = f(2999) + g(999, 3)
#           g(999, 3) = g(999, 'threes') = 0
#       f(4999) = f(3999) + g(999, 4)
#           g(999, 4) = g(999, 'threes') = 0
#       f(5999) = f(4999) + g(999, 5)
#           g(999, 5) = f(999, twos)
# .....



# X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.
#
# A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.
#
# Now given a positive number N, how many numbers X from 1 to N are good?
#
# Example:
# Input: 10
# Output: 4
# Explanation:
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
# Note:
#
# N  will be in range [1, 10000].

import math
class Solution(object):

    nots = set([3, 4, 7])
    musts = set([2, 5, 6, 9])


    def isGoodNumber(self, num):

        MUST_FLAG = False
        totalRemainsFromLeft = 0
        while num > 0:
            firstDigit = math.floor(num/10**math.floor(math.log10(num)))

            if firstDigit in self.nots:
                # increment firstdigit
                # this optimization will jump the number significantly since all numbers with same number of places and this number as digit will not pass
                return totalRemainsFromLeft + (firstDigit+1)*(10**math.floor(math.log10(num))) #700 -> 800, 900 ->

            elif firstDigit in self.musts:
                MUST_FLAG = True

            remainsFromLeft = firstDigit * 10**math.floor(math.log10(num))
            totalRemainsFromLeft += remainsFromLeft
            num = num - remainsFromLeft


        # if fn reaches here then num is a good number | pass True back
        return MUST_FLAG


    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """



        num = 1
        total = 0

        while num <= N:

            checkGoodNum = self.isGoodNumber(num)

            if checkGoodNum == True:
                total += 1
                num += 1
            elif checkGoodNum == False:
                num += 1
                continue
            else:
                num = checkGoodNum
        return total

obj = Solution()
print obj.rotatedDigits(1999) + 2*(obj.rotatedDigits(2999)-obj.rotatedDigits(1999))
print obj.rotatedDigits(2999) + (obj.rotatedDigits(2999)-obj.rotatedDigits(1999))
print obj.rotatedDigits(5999)
# print obj.isGoodNumber(145)