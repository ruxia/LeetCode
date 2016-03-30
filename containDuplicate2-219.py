def containsNearbyDuplicate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        a=dict()
        for i in range(len(nums)):
            if a.has_key(nums[i]):
                if i-a[nums[i]] <= k:
                    return True
            a[nums[i]] = i
        return False

if __name__ == '__main__':
    print(containsNearbyDuplicate([1,2,6,7,3,2,7,1],3))
