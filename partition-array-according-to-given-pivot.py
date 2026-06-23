class Solution(object):
    def pivotArray(self, nums, target):
        less=[]
        eq=[]
        great=[]
        for i in nums:
            if i<target:
                less.append(i)
            elif  i==target:
                eq.append(i)
            else:
                great.append(i)
        return less+eq+great
