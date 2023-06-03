from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        myCounter = Counter(students)

        for sandwich in sandwiches:
            if myCounter[sandwich] == 0:
                break
            else:
                myCounter[sandwich] -= 1
        return myCounter.total()