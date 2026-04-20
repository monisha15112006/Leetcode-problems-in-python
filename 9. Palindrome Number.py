class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        a = 0
        for i in range(int(len(x)/2)):
            if x[i] == x[len(x)-i-1]:
                a += 1
        if a == len(x)/2:
            return True
        else:
            return False
