def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        x= nums1[0:m]
        y= nums2[0:n]
        x.extend(y)
        x.sort()
        nums1[0:m+n]= x
        return nums1

if __name__ == '__main__':
    print(merge([1,4],4,[3,5],2))
