class Solution(object):
    def scoreOfString(self, s):
        r=0
        for i in range(1,len(s)):
            r+=abs(ord(s[i-1])-ord(s[i]))
        return r
