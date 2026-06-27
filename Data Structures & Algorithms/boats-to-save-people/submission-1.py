class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 1,2,2,3,3
        boats = 0
        if len(people) == 0:
            return boats
        
        people.sort()
        l = 0
        r = len(people) - 1
        
        while l <= r:
            if people[l] + people[r] <= limit:
                boats+=1
                l+=1
                r-=1
            elif people[l] + people[r] > limit:
                boats+=1
                r-=1
            elif l == r:
                boats+=1
                break
        return boats
        