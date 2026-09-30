class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each number
        count = Counter(nums)
        
        # Step 2: Create buckets where index = frequency
        # Length is len(nums) + 1 because frequency can range from 0 to len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # Step 3: Gather the top k frequent numbers from highest to lowest frequency
        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res

        