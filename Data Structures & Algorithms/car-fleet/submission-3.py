class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 1
        pos_speed = []
        time_arr = []

        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))
        pos_speed.sort()
        
        for i in pos_speed:
            time = (target - i[0]) / i[1]
            time_arr.append(time)
        
        fleet_time = time_arr[-1]
        for i in range(len(time_arr) - 2, -1, -1):
            if time_arr[i] <= fleet_time:
                continue
            else:
                fleet += 1
                fleet_time = time_arr[i]
        return fleet