#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-11 21:12:07
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # nums=sorted(nums)
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False
        a=dict()
        for x in nums:
            if a.has_key(x):
                a[x]+=1
            else:
                a[x]=1
        for v in a.values():
            if v>1:
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.containsDuplicate([1,2,3,1]))