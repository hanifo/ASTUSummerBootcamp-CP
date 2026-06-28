class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        res = 0
        l = 0

        while l < len(nums):
            if nums[l] % 2 != 0 or nums[l] > threshold:
                l += 1
                continue
            r = l

            while (r < len(nums) and nums[r] <= threshold and (r == l or nums[r] % 2 != nums[r-1] % 2)):
                res = max(res, r - l + 1)
                r += 1
            l = r

        return res
