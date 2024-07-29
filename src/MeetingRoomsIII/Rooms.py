from heapq import heappop, heappush, heapify
from collections import defaultdict
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        free = list(range(n))
        heapify(free)
        
        active = []
        roomMeetings = defaultdict(int)
        
        for start, end in meetings:

            while active and active[0][0] <= start:
                finishT, room = heappop(active)
                heappush(free, room)
            
            if free:

                room = heappop(free)
                heappush(active, (end, room))
            else:
                finishT, room = heappop(active)
                newEnd = finishT + (end - start)
                heappush(active, (newEnd, room))
            
            roomMeetings[room] += 1
        
        max_meetings = max(roomMeetings.values())
        result = min(room for room, count in roomMeetings.items() if count == max_meetings)
        
        return result


solution = Solution()
n = 2
meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]
print(solution.mostBooked(n, meetings))  # saída: 0

n = 3
meetings = [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
print(solution.mostBooked(n, meetings))  # saída: 1