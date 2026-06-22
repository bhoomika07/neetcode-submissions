class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        l = 0
        r = x
        probable_mid = 0

        while l <= r:
            mid = l + (r - l) // 2
            square = (mid)*(mid)
            if square == x:
                return mid
            elif square < x:
                l = mid+1
                probable_mid = mid
            elif square > x:
                r = mid-1
        return probable_mid

        