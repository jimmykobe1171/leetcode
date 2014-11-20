"""
**Problem description:**
    Implement int sqrt(int x).

    Compute and return the square root of x.
"""

class Solution:
    # @param x, an integer
    # @return an integer

    def sqrt(self, x):
        # def bs(target, begin, end):
        #     # print begin, end
        #     if begin > end:
        #         return None

        #     index = (begin + end) / 2.0
        #     approx = index * index
        #     if approx - target >= 1:
        #         return bs(target, begin, index)
        #     elif approx - target <= -1:
        #         return bs(target, index, end)
        #     else:
        #         return index

        def bs(target, begin, end):
            # print begin, end
            if begin > end:
                return end

            index = (begin + end) / 2
            approx = index * index
            if approx - target > 0:
                return bs(target, begin, index-1)
            elif approx - target < 0:
                return bs(target, index+1, end)
            else:
                return index

        ans = bs(x, 0, x)
        return ans


def main():
    target = input('input a number for sqrt calculation: ')
    ans = Solution().sqrt(target)
    print 'answer :' + str(ans)
    ans = round(ans)
    print 'the answer is %f' % ans

if __name__ == '__main__':
    main()
