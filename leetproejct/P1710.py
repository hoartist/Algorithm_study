
class List(object):

    def __init__(self,boxTypes):
        self.boxTypes=boxTypes


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # 박스 유닛으로 오름차순 정렬
        sBoxTypes = sorted(boxTypes, key=lambda x: -x[1])
        cnt = 0
        ans = 0
        for box, unit in sBoxTypes:
            # 박스의 유닛을 곱하기전에 개수 확인
            cnt += box
            if cnt > truckSize:
                # 박스를 싫은 개수가 초과 했을떄,
                # 남은 공간만큼,유닛 계산하여 싫기
                ans += (truckSize - (cnt - box)) * unit
                break
                ans += box * unit
                return res

