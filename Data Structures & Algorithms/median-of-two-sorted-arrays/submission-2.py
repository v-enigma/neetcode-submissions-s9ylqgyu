class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       
        sum = (len(nums1) + len(nums2))
        median = sum//2 + 1
        def findsolution():
            left1 = 0
            right1 = len(nums1)-1
            left2 = 0
            right2 = len(nums2)-1
            found = False

            while not found:
                if left1 > right1 :
                    idx = median - (right1+1) - 1   # 0-based index into nums2
                    if sum % 2 == 0:
                        return (nums2[idx - 1] + nums2[idx]) / 2
                    else:
                        return nums2[idx]

                if left2 > right2:
                    idx = median - (right2+1) - 1   # 0-based index into nums1
                    if sum % 2 == 0:
                        return (nums1[idx - 1] + nums1[idx]) / 2
                    else:
                        return nums1[idx]

                middle1 = (left1 + right1)//2
                middle2 = ( left2 + right2)//2
                total = (middle1 + middle2+2)
                if ( total == median ):
                    if nums1[middle1] >= nums2[middle2]:
                        if middle2+1 >= len(nums2) or nums2[middle2+1] > nums1[middle1]:
                            if (sum%2 == 0) :
                                if middle1> 0 and nums2[middle2] <= nums1[middle1-1]:
                                    m =(nums1[middle1-1]+ nums1[middle1])/2
                                    return m
                                else:
                                    m = ((nums2[middle2] + nums1[middle1])/2)
                                    return m
                            else:
                                return nums1[middle1]
                        else:
                            left2 = middle2+1

                    else :
                        if middle1+1 >= len(nums1) or nums1[middle1+1]> nums2[middle2]:
                            if (sum%2) == 0 :
                                if middle2 > 0 and  (nums2[middle2-1]>= nums1[middle1]):
                                    return (nums2[middle2]+ nums2[middle2-1])/2
                                else:
                                    return (nums2[middle2]+ nums1[middle1])/2
                            else:
                                return nums2[middle2]
                        else:
                            left1 = middle1+1
                elif total < median :
                    if nums1[middle1] <= nums2[middle2]:
                        left1 = middle1+1
                    else:
                        left2 = middle2+1
                else:
                    if nums1[middle1] <= nums2[middle2]:
                        right2 = middle2-1
                    else:
                        right1 = middle1-1
        return findsolution()





