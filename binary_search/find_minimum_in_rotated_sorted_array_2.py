# Find Minimum in Rotated Sorted Array II
"""
**Problem description:**
    Follow up for "Find Minimum in Rotated Sorted Array":
    What if duplicates are allowed?

    Would this affect the run-time complexity? How and why?
    Suppose a sorted array is rotated at some pivot unknown to you beforehand.

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

    Find the minimum element.

    The array may contain duplicates.
"""
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        begin = 0
        end = len(num) - 1
            
        while begin < end:
            if num[begin] < num[end]:
                return num[begin]

            mid = (begin + end) / 2
            if num[begin] < num[mid]:
                begin = mid + 1
            elif num[begin] > num[mid]:
                end = mid
            else:
                begin += 1

        return num[begin]

def main():
    test = [1, 1]
    ans = Solution().findMin(test)
    print ans

if __name__ == '__main__':
    main()