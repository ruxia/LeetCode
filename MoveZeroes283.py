class Solution(object):
    def moveZeroes(self, nums):
        i,j=0,0
        while(j<len(nums)):
            if nums[i]==0:
                while(j<len(nums)-1 and nums[j]==0):
                    j+=1
                nums[i]=nums[j]
                nums[j]=0
            i +=1
            j +=1
        return nums

if __name__ == '__main__':
    s = Solution()
    print(s.moveZeroes([1,2,3,0,4,5,0,0,6,7]))