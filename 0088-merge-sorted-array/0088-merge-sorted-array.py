class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        pos_tracker = m+n-1
        arr1_tracker = m-1
        arr2_tracker = n-1

        while arr1_tracker>=0 and arr2_tracker>=0:

            if nums1[arr1_tracker]>=nums2[arr2_tracker]:
                nums1[pos_tracker] = nums1[arr1_tracker]
                arr1_tracker = arr1_tracker-1
                pos_tracker=pos_tracker-1

            else:
                nums1[pos_tracker] = nums2[arr2_tracker]
                arr2_tracker = arr2_tracker-1
                pos_tracker=pos_tracker-1
        
        if arr2_tracker>=0:
            while arr2_tracker>=0:
                nums1[arr2_tracker] = nums2[arr2_tracker]
                arr2_tracker-=1