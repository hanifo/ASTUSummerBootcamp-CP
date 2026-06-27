class Solution(object):
    def findLHS(self, nums):

        freq={}
        res=0

        for i in nums:
            freq[i]=freq.get(i, 0)+1

        for i in freq:
            if i+1 in freq:
                if res<freq[i]+freq[i+1]:
                    res= freq[i]+freq[i+1]

        return res
