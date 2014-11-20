"""
**Problem description:**
    two integers without using multiplication, division and mod operator.

"""
# Divide Two Integers 

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        new_dividend = dividend if dividend > 0 else -dividend
        new_divisor = divisor if divisor > 0 else -divisor

        count, total_count, accum, total = 1, 1, new_divisor, new_divisor

        if new_divisor > new_dividend:
            return 0

        while total < new_dividend:
            if total + new_divisor > new_dividend:
                break
            elif total + accum <= new_dividend:
                total += accum
                total_count += count
                accum += accum
                count += count
            else:
                total += new_divisor
                total_count += 1
                accum = new_divisor
                count = 1

            # print total, accum, count
        if new_dividend != dividend and new_divisor == divisor:
            total_count = -total_count
        elif new_dividend == dividend and new_divisor != divisor:
            total_count = -total_count

        return total_count

def main():
    ans = Solution().divide(-1006986286, -2145851451)
    print ans

if __name__ == '__main__':
    main()

