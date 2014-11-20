# Find Minimum in Rotated Sorted Array
"""
**Problem description:**
    Suppose a sorted array is rotated at some pivot unknown to you beforehand.

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

    Find the minimum element.

    You may assume no duplicate exists in the array.
"""
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        begin = 0
        end = len(num) - 1
        if num[begin] < num[end]:
            return num[begin]
            
        while begin < end:
            mid = (begin + end) / 2
            if num[mid] < num[end]:
                end = mid
            else:
                begin = mid + 1

        return num[begin]

def main():
    test = [4,5,1,2,3]
    ans = Solution().findMin(test)
    print ans

if __name__ == '__main__':
    main()