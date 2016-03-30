 class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        nums=[[1]]
        for i in range(1,numRows):
            temp = [1]
            for j in range(i-1):
                temp.append(nums[i-1][j]+nums[i-1][j+1])
            temp.append(1)
            nums.append(temp)
        return nums

if __name__ == '__main__':
    s= Solution()
    print(s.generate(5))
