class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        num=''.join(str(number) for number in nums)
        return num.count(str(digit))
