import math
from heapq import heappush,heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Create a minHeap (distance, points)
        min_heap = []
        n = len(points)
        for i in range(n):
            x = points[i][0]
            y = points[i][1]
            dist = self.getDist(x,y)
            heappush(min_heap, [dist,points[i]])

        # Pop from minHeap k times and put the points into the result list
        result = []
        for i in range(k):            
            result.append(heappop(min_heap)[1])
        print(result)

        return result        

    """
    Eucledian distance = math.sqrt((x1-x2)**2+(y1-y1)**2)
    since origin is (0,0)
    distance = math.sqrt(x**2 + y**2)  
    """
    def  getDist(self,x,y):
        return math.sqrt(x**2 + y**2)  
