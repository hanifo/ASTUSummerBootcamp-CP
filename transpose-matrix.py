class Solution(object):
    def transpose(self, matrix):

        row=len(matrix)
        column=len(matrix[0])

        ans=[[0 for i in range(row)] for j in range(column)]
     
        for i in range(column):
            for j in range(row):
                ans[i][j]=matrix[j][i]
        return ans
