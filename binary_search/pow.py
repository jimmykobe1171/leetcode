# leetcode Pow(x, n)

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float

    # n maybe negative
    def pow(self, x, n):
        def bs_pow(x, n):
            if n == 1:
                return x

            if n%2 == 0:
                tmp = bs_pow(x, n/2)
                return tmp * tmp
            else:
                tmp = bs_pow(x, (n-1)/2)
                return x * tmp * tmp
        if x == 0:
            return 0
            
        if n == 0:
            return 1
        elif n > 0:
            return bs_pow(x, n)
        else:
            return 1 / bs_pow(x, -n)

def main():
    ans = Solution().pow(0, -1)
    print ans

if __name__ == '__main__':
    main()