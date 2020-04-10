# Remainder divisor quotient logic
# Another Learning: we have a sorted list and for a given num we want to find list_elem <= num: Optimum way to find - Binary Search


# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
#
# Example 1:
#
# Input: 3
# Output: "III"


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        self.mapIntRoman = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
            4: 'IV',
            9: 'IX',
            40: 'XL',
            90: 'XC',
            400: 'CD',
            900: 'CM'
        }

        self.romanIntsSorted = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

        return self.genPlaceVal(num)

    def genPlaceVal(self, num):
        rest = num
        iter = 1
        roman = ""
        while rest > 0:
            remain = rest % 10
            div = 10 ** (iter - 1)
            rest = int(rest/10)
            val = div*remain
            roman = self.getRoman(val) + roman
            iter += 1
        return roman

    def getRoman(self, decimal):

        if decimal == 0:
            return ''

        if decimal in self.mapIntRoman:
            return self.mapIntRoman[decimal]
        else:
            lowerBound = self.BS(decimal)
            return self.mapIntRoman[lowerBound] + self.getRoman(decimal - lowerBound)

    def BS(self, num):
        if num < 90:
            if num < 10:
                if num < 4:
                    return 1
                else:
                    return 5
            else:
                if num < 40:
                    return 10
                else:
                    return 50
        else:
            if num < 400:
                return 100
            else:
                if num < 900:
                    return 500
                else:
                    return 1000

obj = Solution()
print obj.intToRoman(2000)