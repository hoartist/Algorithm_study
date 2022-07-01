class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda box: box[1], reverse=True)
        stuckCount = 0
        for box in boxTypes:
            while(box[0] > 0):
                if(truckSize <= 0):
                    return stuckCount
                stuckCount += box[1]
                box[0] -= 1
                truckSize -= 1
        return stuckCount