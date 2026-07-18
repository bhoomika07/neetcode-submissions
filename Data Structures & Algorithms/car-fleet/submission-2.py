class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [(4,2) -> 3 mins, (1,3) -> 3 mins]
        position_and_speed_map = {}
        for i in range(len(position)):
            position_and_speed_map[position[i]] = speed[i]
        
        position_and_speed_map = {k: position_and_speed_map[k] for k in sorted(position_and_speed_map, reverse=True)}
    
        fleet_stack = []
        for position, speed in position_and_speed_map.items():
            time = (target-position)/speed
            if not fleet_stack or fleet_stack[-1] < time:
                fleet_stack.append(time)
        return len(fleet_stack)
