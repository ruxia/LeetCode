class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        return Counter(s).items() == Counter(t).items()

if __name__ == '__main__':
    s=Solution()
    print(s.isAnagram("anagram","nagaram"))
