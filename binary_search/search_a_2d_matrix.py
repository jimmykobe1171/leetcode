# leetcode Search a 2D Matrix
"""
**Problem description:**
    Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.
    For example,

    Consider the following matrix::

        [
          [1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ]
        
    Given target = 3, return true.
"""
class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        begin = 0
        step = len(matrix[0])
        end = step * len(matrix) -1

        while begin <= end:
            mid = (begin + end) / 2
            if matrix[mid/step][mid%step] == target:
                return True
            elif matrix[mid/step][mid%step] < target:
                begin = mid + 1
            else:
                end = mid - 1

        return False

def main():
    test_arr = [[1,4,6]]
    ans = Solution().searchMatrix(test_arr, 1)
    print ans

if __name__ == '__main__':
    main()