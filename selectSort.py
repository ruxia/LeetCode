def selectSort(nums):
    for i in range(len(nums)-1):
        smallest=nums[i]
        #j=i+1
        for j in range(i+1,len(nums)):
            if nums[j]<smallest:
                smallest=nums[j]
                small=j
        temp=nums[small]
        nums[small]=nums[i]
        nums[i]=temp
    return nums

if __name__ == '__main__':
    print(selectSort([4,2,3,1,0]))
