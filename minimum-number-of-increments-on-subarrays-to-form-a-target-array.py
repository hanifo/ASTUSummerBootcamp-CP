class Solution(object):
    def minNumberOperations(self, target):
        ans=target[0]
        for i in range(1,len(target)):
            dif=target[i]-target[i-1]
            if dif >0:
                ans+=dif
        return ans
