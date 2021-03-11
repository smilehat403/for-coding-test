import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        for i in range(len(nums)+1):
            for subset in itertools.combinations(nums,i):
                output.append(list(subset))
        return output