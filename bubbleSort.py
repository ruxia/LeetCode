def bubbleSort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1,i,-1):
            if nums[j]<nums[j-1]:
                temp=nums[j-1]
                nums[j-1]=nums[j]
                nums[j]=temp
    return nums

if __name__ == '__main__':
    print(bubbleSort([4,2,3,1,0]))
