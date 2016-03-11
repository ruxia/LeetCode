class Solution(object):
    def singleNumber(self, nums):
        # d=dict()
        # for x in nums:
        #     if d.has_key(x):
        #         d[x]+=1
        #     else:
        #         d[x]=1
        # for x in nums:
        #     if d[x]==1:
        #         return x
        s=0
        for x in nums:
            s=s^x
        return s

if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([1,2,3,1,2]))