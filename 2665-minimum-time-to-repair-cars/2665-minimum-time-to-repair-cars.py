class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def isValid(mid: int) -> int:
            return sum(int(sqrt(mid // r)) for r in ranks) >= cars
                
        l, r = 1, min(ranks) * pow(cars, 2)
        while r > l:
            mid = (r + l) // 2
            if isValid(mid):
                r = mid
            else:
                l = mid + 1
        return l