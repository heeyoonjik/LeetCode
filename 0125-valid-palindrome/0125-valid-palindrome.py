class Solution(object):
    def isPalindrome(self, s):
        # using slicing
        s = s.lower()

        # filter out unnecessary character with regular expression
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1] # slicing
        