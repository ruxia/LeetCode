class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        newlist=list()
        temp=0
        for i in range(len(nums)):
            if i == len(nums)-1 or nums[i+1]-nums[i] != 1:
                if i-temp >=1:
                    newlist.append(str(nums[temp]) + "->" + str(nums[i]))
                else:
                    newlist.append(str(nums[i]))
                temp=i+1
        return newlist

if __name__ == '__main__':
    s=Solution()
    print(s.summaryRanges([0,1,2,4,5,7]))
