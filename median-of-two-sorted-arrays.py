# Time:  O(log(min(m, n)))
# Space: O(1)
# 
# There are two sorted arrays A and B of size m and n respectively. 
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#

class Solution(object):
    def findMedianSortedArrays(self, A, B):
        lenA, lenB = len(A), len(B)
        if (lenA + lenB) % 2 == 1: 
            return self.getKth(A, B, (lenA + lenB)/2 + 1)
        else:
            return (self.getKth(A, B, (lenA + lenB)/2) + self.getKth(A, B, (lenA + lenB)/2 + 1)) * 0.5
            
    def getKth(self, A, B, k):
        m, n = len(A), len(B)
        if m > n:
            return self.getKth(B, A, k)
            
        left, right = 0, m    
        while left < right:
            mid = left + (right - left) / 2
            j = k - 1 - mid
            if 0 <= j < n and A[mid] >= B[j]:
                right = mid
            else:
                left = mid + 1
            
        Ai_minus_1, Bj = float("-inf"), float("-inf")
        if left - 1 >= 0:
            Ai_minus_1 = A[left - 1]
        if k - 1 - left >= 0:
            Bj = B[k - 1 - left]
        
        return max(Ai_minus_1, Bj)
