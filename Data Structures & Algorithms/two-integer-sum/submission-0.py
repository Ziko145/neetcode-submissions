class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            
            # If the complement exists in our map, we found the pair
            if complement in num_to_index:
                return [num_to_index[complement], index]
            
            # Otherwise, save the current number and its index to the map
            num_to_index[num] = index

        