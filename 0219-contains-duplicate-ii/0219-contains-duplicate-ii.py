class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}

        for index, num in enumerate(nums):
            if num in hm:
                # Check if the difference between indices is at most k
                if index - hm[num] <= k:
                    return True
            # Update the dictionary with the latest index of the number
            hm[num] = index

        return False
