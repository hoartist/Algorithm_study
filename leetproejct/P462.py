class List(object):

    def __init__(self,nums):
        self.nums=nums

class Solution:
    def minMoves2(self,nums:List[int])->int:
        nums=sorted(nums)
        left,right=0,len(nums)-1
        result=0
        while left<right:
            result+=nums[right]-nums[left]
            left,right=left+1,right-1
            return result