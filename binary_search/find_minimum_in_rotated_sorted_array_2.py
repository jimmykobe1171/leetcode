# Find Minimum in Rotated Sorted Array II

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        begin = 0
        end = len(num) - 1
            
        while begin < end:
            mid = (begin + end) / 2
            print mid
            if num[mid] < num[end]:
                end = mid
            elif num[mid] > num[end]:
                begin = mid + 1
            else:
                end -= 1

        return num[begin]

def main():
    test = [1, 1, 5, 1]
    ans = Solution().findMin(test)
    print ans

if __name__ == '__main__':
    main()