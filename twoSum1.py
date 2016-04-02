class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a=dict()
        newlist=list()
        for i in range(len(nums)):
            if a.has_key(target-nums[i]):
                newlist.append(i)
                newlist.append(a[target-nums[i]])
                break
            a[nums[i]] = i
        return newlist

if __name__ == '__main__':
    s=Solution()
    print(s.twoSum([0,3,2,4,0],0))
