# leetcode Search Insert Position

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
        