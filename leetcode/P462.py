class Solution:
    def getAvg(self, nums:List[int]) -> int:
        return int(sum(nums) / len(nums))
    
    def minMoves2(self, nums: List[int]) -> int:
        # 평균으로 접근하려고 했으나 TC에서 오답처리됨

        # 반례)[1,0,0,8,6]
        
        # avg = self.getAvg(nums)
        # if avg == 0:
        #     avg = 1
        # answer = 0
        # for n in nums:
        #     answer += abs(avg - n)
        # return answer
        
        nums.sort()
        
        m = nums[len(nums) // 2]
        
        answer = 0
        for i in nums:
            answer += abs(m - i)
        return answer

            