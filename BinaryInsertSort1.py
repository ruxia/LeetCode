def BinaryInsertSort(nums):
    for i in range(1,len(nums)):
        left=0
        right=i-1
        temp=nums[i]
        while left<=right:
            middle=(left+right)/2
            if temp<=nums[middle]:
                right=middle-1
            else:
                left=middle+1
        for i in range(i-1,left-1,-1):
            nums[i+1]=nums[i]
        nums[left]=temp
    return nums

if __name__ == '__main__':
    print(BinaryInsertSort([4,2,1,3,0]))
