# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
#
# Example 1:
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# Note:
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


class Solution(object):

    dpDigitMult = {}
    dpDigit = {}

    def multiplyDigits(self, a, b):

        if a < b:
            small = a
            big = b
        else:
            small = b
            big = a

        # if we already multiplied the digits in the past and is stored, simply return the multiplication
        if (small, big) in self.dpDigitMult:
            return self.dpDigitMult[(small, big)]

        # else, calculate
        smallNum, bigNum = 0, 0
        if small not in self.dpDigit:
            while str(smallNum) != small:
                smallNum += 1
            self.dpDigit[small] = smallNum
        else:
            smallNum = self.dpDigit[small]

        if big not in self.dpDigit:
            while str(bigNum) != big:
                bigNum += 1
            self.dpDigit[big] = bigNum
        else:
            bigNum = self.dpDigit[big]

        mult = smallNum * bigNum
        self.dpDigitMult[(small, big)] = mult

        return mult

    def multiplyNumberDigit(self, bigNum, smallChar):
        mult = 0
        carry = 0
        tens = 1

        for i in range(len(bigNum)):
            bigChar = bigNum[-i-1]
            tempMult = self.multiplyDigits(smallChar, bigChar) + carry
            if tempMult >= 10:
                ones = tempMult % 10
                carry = tempMult / 10
            else:
                ones = tempMult
                carry = 0
            mult += tens * ones

            # update tens
            tens *= 10
        if carry != 0:
            mult += tens*carry

        return mult


    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if len(num1) < len(num2):
            small = num1
            big = num2
        else:
            small = num2
            big = num1

        # final multiplicaton output
        mult = 0
        tens = 1
        multStages = []
        carry = 0

        for i in range(len(small)):
            smallChar = small[-i-1]
            tempMult = self.multiplyNumberDigit(big, smallChar)
            multStages.append(tempMult)

            stageAdd = 0

            # for all the multiplication stages stored, add their ones place
            if i != len(small):
                for j in range(len(multStages)):
                    elm = multStages[j]
                    ones = (elm % 10)

                    # if not last iteration
                    stageAdd += ones
                    multStages[j] = elm / 10


            stageAdd += carry
            if stageAdd >= 10:
                ones = stageAdd % 10
                carry = stageAdd / 10
            else:
                ones = stageAdd
                carry = 0

            mult += ones * tens
            tens *= 10
                    # else:
                    #




        # if carry > 0:
        #     mult += carry * tens
        mult += (sum(multStages)+carry) * tens

        return str(mult)


obj = Solution()
# print obj.multiplyDigits('0', '3')
# print obj.multiplyDigits('3', '2')
# print obj.multiplyDigits('3', '6')
# print obj.multiplyNumberDigit('123', '9')
# print obj.multiply('121', '0')
print obj.multiply("123", "456")
print obj.dpDigitMult