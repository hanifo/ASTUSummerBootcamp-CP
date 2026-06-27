class Solution(object):
    def findMaxAverage(self, nums, k):
        current = sum(nums[:k])
        ave = current / float(k)
        l = 0
        while l + k < len(nums):
            current -= nums[l]
            current += nums[l+k]
            ave = max(ave, current / float(k))
            l += 1
        return ave
