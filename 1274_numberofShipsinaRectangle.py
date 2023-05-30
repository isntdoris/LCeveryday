# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def findShips(topRight, bottomLeft): # helper functions
            # terminal conditions
            if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y:
                return 0
            elif topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
                return int(sea.hasShips(topRight, bottomLeft))

            if not sea.hasShips(topRight, bottomLeft):
                return 0
            
            midX = (topRight.x + bottomLeft.x) // 2
            midY = (topRight.y + bottomLeft.y) // 2
            mid = Point(midX, midY)

            topLeftQ = findShips(Point(mid.x, topRight.y), Point(bottomLeft.x, mid.y + 1))
            topRightQ = findShips(topRight, Point(mid.x + 1, mid.y + 1))
            bottomLeftQ = findShips(Point(mid.x, mid.y), bottomLeft)
            bottomRightQ = findShips(Point(topRight.x, mid.y), Point(mid.x + 1, bottomLeft.y))

            return topLeftQ + topRightQ + bottomLeftQ + bottomRightQ
        
        return findShips(topRight, bottomLeft)