# leetcode Median of Two Sorted Arrays O(log(m+m))

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        MAX = 100000000
        MIN = -100000000
        def find_kth_sorted_arrays(A, begin_a, end_a, B, begin_b, end_b, k):
            # print A, begin_a, end_a, B, begin_b, end_b, k
            if begin_a > end_a:
                return B[begin_b+k-1]
            elif begin_b > end_b:
                return A[begin_a+k-1]
            # here we must maintain the invariant: i + j -1 = k
            i = k/2
            j = k - i - 1
            # print i, j
            # edge case checking
            A_i = MAX if end_a - begin_a < i else A[begin_a+i]
            B_j = MAX if end_b - begin_b < j else B[begin_b+j]
            if i-1 < 0:
                A_i_1 = MIN
            elif end_a - begin_a < i - 1:
                A_i_1 = MAX
            else:
                A_i_1 = A[begin_a+i-1]

            if j-1 < 0:
                B_j_1 = MIN
            elif end_b - begin_b < j - 1:
                B_j_1 = MAX
            else:
                B_j_1 = B[begin_b+j-1]
            # A_i_1 = MIN if i-1 < 0 else A[begin_a+i-1]
            # B_j_1 = MIN if j-1 < 0 else B[begin_b+j-1]
            # found k
            if B_j_1 <= A_i and A_i <= B_j:
                return A_i
            elif A_i_1 <= B_j and B_j <= A_i:
                return B_j
            # not found k
            if A_i <= B_j:
                # exclude A[begin_a] to A[begin_a+i]
                # exclued B[begin_b+j] to B[end_b]
                begin_a += i+1
                end_b = end_b if B_j_1 == MAX else  begin_b+j-1
                return find_kth_sorted_arrays(A, begin_a, end_a, B, begin_b, end_b, k-i-1)
            elif B_j <= A_i:
                # exclude B[begin_b] to B[begin_b+j]
                # exclued A[begin_a+i] to A[end_a]
                end_a = end_a if A_i_1 == MAX else begin_a+i-1
                begin_b += j+1
                return find_kth_sorted_arrays(A, begin_a, end_a, B, begin_b, end_b, k-j-1)

        k = (len(A) + len(B))/2
        if (len(A) + len(B)) % 2 == 0:
            ans = (find_kth_sorted_arrays(A, 0, len(A)-1, B, 0, len(B)-1, k) + find_kth_sorted_arrays(A, 0, len(A)-1, B, 0, len(B)-1, k+1))/2.0
        else:
            ans = float(find_kth_sorted_arrays(A, 0, len(A)-1, B, 0, len(B)-1, k+1))
        # print k
        return ans

def main():
    # A = [2]
    A = []
    # B = [1]
    B = [1,2,3,4,5]
    ans = Solution().findMedianSortedArrays(A, B)
    print ans

if __name__ == '__main__':
    main()