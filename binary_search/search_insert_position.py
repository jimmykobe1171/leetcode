# -*- coding: utf-8 -*-
"""
**Problem description:**
    Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

    You may assume no duplicates in the array.

    Here are few examples::

        [1,3,5,6], 5 → 2
        [1,3,5,6], 2 → 1
        [1,3,5,6], 7 → 4
        [1,3,5,6], 0 → 0

"""
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        def bs(target, array, begin, end):
            if begin > end:
                return begin
            
            index = (begin + end)/2
            tmp = array[index]
            if tmp == target:
                return index
            elif tmp > target:
                return bs(target, array, begin, index-1)
            else:
                return bs(target, array, index+1, end)
                
        return bs(target, A, 0, len(A)-1)
        