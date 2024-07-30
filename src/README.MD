# 1094. Car Pooling

Problema: [Car Pooling](https://leetcode.com/problems/car-pooling/description/)

**Descrição:** <br>
There is a car with **capacity** empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer **capacity** and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.



**Example 1:**<br>
**Input:** trips = [[2,1,5],[3,3,7]], capacity = 4<br>
**Output:** false

**Example 2:** <br>
**Input:** trips = [[2,1,5],[3,3,7]], capacity = 5<br>
 **Output:** true


## Solução

Como no final o objetivo deste problema é saber se é possivel ou não realizar todas as viagens sem exceder a capacidade do carro, é possivel utilizar o algoritmo de interval partitioning. 
<br>**Exemplo:**

```Python
class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        events = []
        for trip in trips:
            numP, start, end = trip
            events.append((start, numP))  
            events.append((end, -numP))
        events.sort(key=lambda x: (x[0], x[1]))  
```

Primiro é criado uma lista vazia e depois nela é separada os eventos de **pickup** e **dropoff** e depois ordena eles por tempo, com desempate de pickups antes dos de dropoff.

```Python
        currP = 0
        for event in events:
            time, passChange = event
            currP += passChange
            if currP > capacity:
                return False
        return True
```
Após isso o número de passageiros é inicializado, e o código começa a iterar nos eventos, ele também verifica se a capacidade do carro for excedida, se sim ele retorna **False** se não **True** 


**Submissão:**<br>
![](./assets/Sub11.png)

# 435. Non-overlapping Intervals

Problema: [Média: 435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/description/)

**Descrição:** <br>

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

**Example 1:**

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]<br>
Output: 1 <br>
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

**Example 2:**

Input: intervals = [[1,2],[1,2],[1,2]] <br>
Output: 2 <br>
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

## Solução


Para a solução desse problema foi usado o método de algoritmo ambicioso interval scheduling. Onde foi feito a ordenação do vetor interval pelo fim (end), depois é avaliado se o segundo intervalo intersecta com o primeiro, se sim ele não faz nada, se não ele ele soma a quantidade de intervalos que não se intersectam em +1 e troca o fim base. No final é subtraído a quantidade de intervalos que não se intersectam pela a quantidade total de intervalos, e este é o resultado.

```python
def overlapping(intervals):  
    intervals.sort(key=lambda x: x[1])  
    count = 1
    end = intervals[0][1]  
    for i in range(1, len(intervals)):
        if intervals[i][0] >= end:
            count += 1
            end = intervals[i][1]  
    return len(intervals) - count
```

**Exemplo:**

![](./assets/exemploOverlapping.png)

**Submissão:**<br>

![](./assets/Sub22.png)

# 2402. Meeting Rooms III

Problema: [Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/description/)

**Descrição:**

You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.


**Example 1:**

**Input:** n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]<br>
**Output:** 0<br>
**Explanation:**<br>
- At time 0, both rooms are not being used. The first meeting starts in room 0.
- At time 1, only room 1 is not being used. The second meeting starts in room 1.
- At time 2, both rooms are being used. The third meeting is delayed.
- At time 3, both rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
- At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
Both rooms 0 and 1 held 2 meetings, so we return 0.<br><br> 

**Example 2:**

**Input:** n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]<br>
**Output:** 1<br>
**Explanation:**<br>
- At time 1, all three rooms are not being used. The first meeting starts in room 0.
- At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
- At time 3, only room 2 is not being used. The third meeting starts in room 2.
- At time 4, all three rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
- At time 6, all three rooms are being used. The fifth meeting is delayed.
- At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1. 

## Solução

Para resolver este problema,foi implementado uma solução usando como base algoritmo ambicioso de interval partitioning <br>


```Python
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        free = list(range(n))
        heapify(free)
        
        active = []
        roomMeetings = defaultdict(int)
```

Nesse caso primeiro foi ordenado as reuniões pelo seu tempo de início e depois foi inicializado um heap de salas disponíveis e outro para as salas em uso e também um contador de reuniões por sala.

```Python
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
```
Após isso o resto do interval partitioning é usado, iterando nas reuniões, liberando as salas com reuniões terminadas, alocar as reuniões nas salas livres, atrasar a reunião caso não tenha sala ele incrementa o contador das reuniões em cada sala, depois ele encontra a sala que teve mais reuniões e retorna ela .



**Submissão:**


![](./assets/Sub21.png)

# 135. Candy

Problema: [135. Candy](https://leetcode.com/problems/candy/submissions/1337823294/)<br>
![](./src/assets/Sub12.png)

**Descrição:** <br>
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

**Example 1:**

Input: ratings = [1,0,2] <br>
Output: 5 <br>
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.


**Example 2:**

Input: ratings = [1,2,2] <br>
Output: 4 <br>
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

## Solução

Foi usado o algorítimo ambicioso two-pass para resolver essa questão. Ele consiste em passar duas vezes (forward e backward pass) em um array comparando os valores somente uma vez com o vizinho de um lado, e depois do outro. Isso garante a melhor solução O(n) porque ele só percorre o vetor 2 vezes.

```Python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        
        # Forward pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Backward pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)
          
```

**Submissão:**<br>
![](./assets/Sub12.png)
