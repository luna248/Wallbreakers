"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        if not employees:
            return 0

        totalImportance = 0
        allSubordinates = [id]

        while allSubordinates:
            currEmployee = allSubordinates.pop()

            #this for loop will parse through all the nodes from the same level currently
            #in the deque
            for i in range(len(employees)):
                if employees[i].id == currEmployee:
                    currEmployee= i
                    totalImportance += employees[i].importance
                    break

                #add all children of the node to the deque
            if employees[currEmployee].subordinates:
                for i in employees[currEmployee].subordinates:
                    allSubordinates.append(i)


        return totalImportance
        
