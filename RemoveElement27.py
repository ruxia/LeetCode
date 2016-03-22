class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # nums[:]=[x for x in nums if x!=val]
        # return len(nums)

        j=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[j]=nums[i]
                j=j+1
        return j

if __name__ == '__main__':
    s=Solution()
    print(s.removeElement([3,4,5],4))
