class Solution(object):
    def reverseWords(self, s):
        lst = s.split()

        for i in range(len(lst)):
            lst[i] = lst[i][::-1]

        return " ".join(lst)
