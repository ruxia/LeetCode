def mergeSort(nums):
    sort(nums,0,len(nums)-1)
    return nums

def sort(nums,left,right):
    if left < right:
        center=(left+right)/2
        sort(nums,left,center)
        sort(nums,center+1,right)
        merge(nums,left,center,right)

def merge(nums,left,center,right):
    newlist=list()
    temp,middle=left,center+1
    while left<=center and middle<=right:
        if nums[left]<nums[middle]:
            newlist.append(nums[left])
            left+=1
        else:
            newlist.append(nums[middle])
            middle+=1
    while middle<=right:
        newlist.append(nums[middle])
        middle+=1
    while left<=center:
        newlist.append(nums[left])
        left+=1
    for i in newlist:
        nums[temp]=i
        temp+=1

if __name__ == '__main__':
    print(mergeSort([4,2,3,1,0]))
