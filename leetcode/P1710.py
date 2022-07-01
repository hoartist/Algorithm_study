class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda box: box[1], reverse=True)
        stuckCount = 0
        for box in boxTypes:
            if(truckSize <= 0): break
            
            while(box[1] > 0):
                if(truckSize <= 0):
                    break
                stuckCount += box[0]
                box[1] -= 1
                truckSize -= 1
                
        print(stuckCount)