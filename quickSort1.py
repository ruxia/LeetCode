def quickSort(nums):
    if len(nums)>0:
        sort(nums,0,len(nums)-1)
    return nums

def sort(nums,low,high):
    if low<high:
        pivot=getPivot(nums,low,high)
        sort(nums,low,pivot-1)
        sort(nums,pivot+1,high)

def getPivot(nums,low,high):
    temp=nums[low]
    while low<high:
        while low<high and nums[high]>temp:
            high-=1
        nums[low]=nums[high]
        while low<high and nums[low]<temp:
            low+=1
        nums[high]=nums[low]
    nums[low]=temp
    return low

if __name__ == '__main__':
    print(quickSort([4,2,3,1,0]))
