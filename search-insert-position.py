class Solution(object):
    def searchInsert(self, nums, target):
        if target < nums[0]:
            return 0
        elif target > nums[len(nums) - 1]:
            return len(nums)
        l = 0
        r = len(nums) - 1
        while l <= r:
            if target == nums[l]:
                return l
            elif target == nums[r]:
                return r
            else:
                mid = (l + r) // 2
                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return l
