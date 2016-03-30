class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0
        k=1
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                nums[k] = nums[i + 1]
                k+=1
        return k

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,2]))
