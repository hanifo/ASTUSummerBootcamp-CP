class Solution(object):
    def countPairs(self, nums, target):
        cnt=0
        for i in range (1,len(nums)):
            for j in range (i,len(nums)):
                if nums[i-1]+nums[j]<target:
                    cnt+=1
        return cnt
