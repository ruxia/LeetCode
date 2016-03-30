class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return None
        res = [1]
        for i in range(rowIndex):
            for j in range(i, 0, -1):
                res[j] = res[j-1] + res[j]
            res.append(1)
        return res

if __name__ == '__main__':
    s = Solution()
    print s.getRow(3)
