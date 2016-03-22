def heapSort(nums):
    for i in range(len(nums)-1):
        buildMaxHeap(nums,len(nums)-1-i)
        swap(nums,0,len(nums)-1-i)
    print(nums)

def swap(nums,i,j):
    temp=nums[i]
    nums[i]=nums[j]
    nums[j]=temp

def buildMaxHeap(nums,lastIndex):
    for i in range((lastIndex-1)/2,-1,-1):
        k=i
        while k*2+1 <= lastIndex:
            biggerIndex=2*k+1
            if biggerIndex<lastIndex and nums[biggerIndex]<nums[biggerIndex+1]:
                biggerIndex+=1
            if nums[biggerIndex]>nums[k]:
                swap(nums,k,biggerIndex)
                k=biggerIndex
            else:
                break

if __name__ == '__main__':
    heapSort([4,2,3,1,0])
