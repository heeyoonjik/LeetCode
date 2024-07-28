class Solution(object):
    def isPalindrome(self, s):
        strs = []

        # preprocessing (because of Alphanumeric characters codition)
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # is palindrome checker
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True
        