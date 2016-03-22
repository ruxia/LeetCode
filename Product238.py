class Solution(object):
    def productExceptSelf(self, nums):
        result = []
        product=1
        for i in range(0,len(nums)):
            result.append(product)
            product= product*nums[i]
        product=1
        for j in range(len(nums)-1, -1, -1):
            result[j]=result[j]*product
            product=product*nums[j]
        return result

if __name__ == '__main__':
    s=Solution()
    print(s.productExceptSelf([1,2,3,4]))