import math
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # a = dict()
        # for x in nums:
        #     if a.has_key(x):
        #         a[x]+=1
        #     else:
        #         a[x]=1
        # for k,v in a.items():
        #     if v>0.5*len(nums):
        #         return k
        s=sorted(nums)
        return s[len(nums)/2]

if __name__ == '__main__':
    s=Solution()
    print(s.majorityElement([2,2,2,2,3,3,4]))