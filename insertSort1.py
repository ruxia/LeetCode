def insertSort(nums):
    for i in range(1,len(nums)):
        temp=nums[i]
        j=i-1
        while temp<= nums[j] and j>=0:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=temp
    return nums

if __name__ == '__main__':
    print(insertSort([4,2,1,3,0]))
