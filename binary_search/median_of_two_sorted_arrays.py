# leetcode Median of Two Sorted Arrays O(log(m+m))

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        import sys
        MAX = sys.maxint
        MIN = -1000
        def find_kth_sorted_arrays(A, begin_a, end_a, B, begin_b, end_b, k):
            print A, begin_a, end_a, B, begin_b, end_b, k
            # here we must maintain the invariant: i + j -1 = k
            i  = k/2
            j = k - i - 1
            print i, j
            # edge case checking
            A_i = MAX if end_a - begin_a < i else A[begin_a+i]
            B_j = MAX if end_b - begin_b < j else B[begin_b+j]
            A_i_1 = MIN if i-1 < 0 else A[begin_a+i-1]
            B_j_1 = MIN if j-1 < 0 else B[begin_b+j-1]
            # found k
            if B_j_1 < A_i and A_i < B_j:
                return A_i
            elif A_i_1 < B_j and B_j < A_i:
                return B_j
            # not found k
            if A_i < B_j:
                # exclude A[begin_a] to A[begin_a+i-1]
                # exclued B[begin_b+j] to B[end_b]
                return find_kth_sorted_arrays(A, begin_a+i, end_a, B, begin_b, begin_b+j-1, k-i)
            elif B_j < A_i:
                # exclude B[begin_b] to B[begin_b+j-1]
                # exclued A[begin_a+i] to A[end_a]
                return find_kth_sorted_arrays(A, begin_a, begin_a+i-1, B, begin_b+j, end_b, k-j)

        k = 9
        return find_kth_sorted_arrays(A, 0, len(A)-1, B, 0, len(B)-1, k)

def main():
    A = [1, 3, 5, 7, 8, 9]
    B = [2, 4, 6]
    ans = Solution().findMedianSortedArrays(A, B)
    print ans

if __name__ == '__main__':
    main()