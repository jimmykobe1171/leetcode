# leetcode Search in Rotated Sorted Array

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer

    # wrong solution of O(n)
    # def search(self, A, target):
    #     def revert_array(A):
    #         reverted = A
    #         index = None
    #         for i in range(0, len(A)-1):
    #             if A[i] > A[i+1]:
    #                 index = i
    #         if index != None:
    #             reverted = A[index+1:] + A[:index+1]
    #         return reverted, index
            
    #     def bs(target, array, begin, end):
    #         if begin > end:
    #             return -1
                
    #         index = (begin + end)/2
    #         tmp = array[index]
    #         if tmp > target:
    #             return bs(target, array, begin, index-1)
    #         elif tmp < target:
    #             return bs(target, array, index+1, end)
    #         else:
    #             return index
        
    #     reverted, index = revert_array(A)
    #     ans = bs(target, reverted, 0, len(A)-1)
    #     if ans != -1 and index != None:
    #         if target in A[:index+1]:
    #             ans -= len(A)-1-index
    #         else:
    #             ans += index+1

    #     return ans

    def search(self, A, target):
        def bs(target, array, begin, end):
            if begin > end:
                return -1
                
            mid = (begin + end)/2
            if target == array[mid]:
                return mid

            if array[begin] <= array[mid]:
                if array[begin] <= target and target < array[mid]:
                    return bs(target, array, begin, mid-1)
                else:
                    return bs(target, array, mid+1, end)
            else:
                if array[mid] < target and target <= array[end]:
                    return bs(target, array, mid+1, end)
                else:
                    return bs(target, array, begin, mid-1)

        ans = bs(target, A, 0, len(A)-1)
        return ans

    # not duplicated value
    def search_for_rotation_pivot(self, A):
        ans = -1
        begin = 0
        end = len(A)-1
        while A[begin] > A[end]:
            mid = (begin + end)/2
            # if A[begin] < A[mid]:
            #     begin = mid
            # elif A[begin] > A[mid]:
            #     end = mid-1
            # else:
            #     end = mid
            # ans = end

            if A[mid] > A[end]:
                begin = mid + 1
            else:
                end = mid

        return begin - 1


def main():
    test_cases = []
    test_cases.append([1]) # -1
    test_cases.append([1,2])  # -1
    test_cases.append([2,1])  # 0
    test_cases.append([1,2,3]) # -1
    test_cases.append([3,1,2]) # 0
    test_cases.append([2,3,1]) # 1
    test_cases.append([1,2,3,4,5]) # -1
    test_cases.append([2,3,4,5,1]) # 3
    test_cases.append([3,4,5,1,2]) # 2
    test_cases.append([4,5,1,2,3]) # 1
    # test_arr = [7,3,4,5,6]
    # test_arr = [1,3,4,5,6]
    # ans = Solution().search(test_arr, 2)
    for test_case in test_cases:
        ans = Solution().search_for_rotation_pivot(test_case)
        print ans

if __name__ == '__main__':
    main()