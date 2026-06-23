class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        res=[]
        l,r=0,len(nums)-1
        while l<r:
            res.append(nums[l]+nums[r])
            l,r=l+1,r-1
        return max(res)
