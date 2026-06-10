class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        unique_triplets = set()
        for i in range(len(nums)):
            hash_set = set()
            for j in range(i+1,len(nums)):
                third = -(nums[i]+ nums[j])
                if third in hash_set:
                    triplet = tuple(sorted((nums[i], third, nums[j])))
                    unique_triplets.add(triplet)
                hash_set.add(nums[j])
        res = [list(t) for t in unique_triplets]
        return (res)