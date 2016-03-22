import math
def shellSort(nums):
    d=len(nums)
    while d > 1:
        d=int(math.ceil(d/2))
        for x in range(d):
            for i in range(x+d,len(nums),d):
                temp=nums[i]
                j=i-d
                while j>=0 and temp<nums[j]:
                    nums[j+d]=nums[j]
                    j-=d
                nums[j+d]=temp
    return nums

if __name__ == '__main__':
    print(shellSort([4,2,3,1,0]))
