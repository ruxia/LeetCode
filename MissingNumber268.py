class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None:
            return None
        s= (len(nums)) *(len(nums)+1) / 2
        return s-sum(nums)

        # a = dict()
        # for x in nums:
        #     a[x]=True
        # for k,v in a.items():
        #     if a[k]!=True:
        #         return a[k]

if __name__ == '__main__':
    s= Solution()
    print(s.missingNumber([0]))
