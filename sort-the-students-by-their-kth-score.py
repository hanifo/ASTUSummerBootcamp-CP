class Solution(object):
    def sortTheStudents(self, score, k):
        temp=[]
        for i in score:
            temp.append(i[k])
        temp.sort()
        temp.reverse()
        for i in score:
            c=i[k]
            temp[temp.index(c)]=i
        return temp
