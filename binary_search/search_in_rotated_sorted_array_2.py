# leetcode Search in Rotated Sorted Array

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer

    def search(self, A, target):
        def bs(target, array, begin, end):
            if begin > end:
                return False
                
            mid = (begin + end)/2
            if target == array[mid]:
                return True

            if array[begin] < array[mid]:
                if array[begin] <= target and target < array[mid]:
                    return bs(target, array, begin, mid-1)
                else:
                    return bs(target, array, mid+1, end)
            elif array[begin] > array[mid]:
                if array[mid] < target and target <= array[end]:
                    return bs(target, array, mid+1, end)
                else:
                    return bs(target, array, begin, mid-1)
            else:
                return bs(target, array, begin+1, end)

        ans = bs(target, A, 0, len(A)-1)
        return ans

def main():
    test_arr = [1,1,1,1,5,1]
    ans = Solution().search(test_arr, 2)
    print ans

if __name__ == '__main__':
    main()