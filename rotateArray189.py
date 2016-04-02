class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        self.rotateNums(nums,0,len(nums) - 1 - k)
        self.rotateNums(nums,len(nums) - k, len(nums)-1)
        self.rotateNums(nums,0,len(nums)-1)
        return nums

    def rotateNums(self,nums,left,right):
        while left<=right:
            temp=nums[right]
            nums[right]=nums[left]
            nums[left]=temp
            left+=1
            right-=1

if __name__ == '__main__':
    s=Solution()
    print(s.rotate([1,2,3,4,5,6,7],3))
