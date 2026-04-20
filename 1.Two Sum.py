class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store: { value: index }
        prev_map = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            
            # If the difference exists in the map, we found the solution
            if diff in prev_map:
                return [prev_map[diff], i]
            
            # Otherwise, add current number to the map
            prev_map[n] = i
            
        return []
