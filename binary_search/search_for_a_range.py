# leetcode Search for a Range
"""
**Problem description:**
    Given a sorted array of integers, find the starting and ending position of a given target value.

    Your algorithm's runtime complexity must be in the order of O(log n).

    If the target is not found in the array, return [-1, -1].

    For example,
    Given [5, 7, 7, 8, 8, 10] and target value 8,
    return [3, 4].
"""
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        def bs_range_begin(target, array):
            begin = 0
            end = len(array)
            while begin < end:
                mid = (begin + end)/2
                if array[mid] < target:
                    begin = mid + 1
                else:
                    end = mid
            return begin

        def bs_range_end(target, array):
            begin = 0
            end = len(array)
            while begin < end:
                mid = (begin + end)/2
                if array[mid] <= target:
                    begin = mid + 1
                else:
                    end = mid
            return end - 1

        begin_index = bs_range_begin(target, A)
        end_index = bs_range_end(target, A)
        if begin_index > end_index:
            begin_index = -1
            end_index = -1
        return [begin_index, end_index]

def main():
    test_arr = [1,2,3,4,4,6]
    ans = Solution().searchRange(test_arr, 5)
    print ans

if __name__ == '__main__':
    main()