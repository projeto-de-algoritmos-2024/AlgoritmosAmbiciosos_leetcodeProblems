class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        events = []
        for trip in trips:
            numP, start, end = trip
            events.append((start, numP))  
            events.append((end, -numP))   
        events.sort(key=lambda x: (x[0], x[1]))
        currP = 0
        for event in events:
            time, passChange = event
            currP += passChange
            if currP > capacity:
                return False
        return True

solution = Solution()    
trips = [[2, 1, 5], [3, 3, 7], [3, 6, 8]]
capacity = 4
print(solution.carPooling(trips, capacity))  # saída: False