class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        see =  {}
        for x in range(len(nums)):
            num = nums[x]
            nahom = target - num
            if nahom not in see:
                see[num] = x
            else:
                return [see[nahom], x ]





