"""
Employee system

Given two employee ids, return the managers or leaders shared by two employees in the given data.

                                              CEO (1)
                            /                                                       \
                    Director1 (2)                                               Director2 (5)
               /                  \                                            /             \
        Manager1 (3)                 Manager2 (4)                        Manager3 (6)        Manager4 (7)
        /         \                   /         \                         /        \
Employee1 (8)  Employee2 (9)   Employee3 (10)   Employee4 (11)   Employee5 (12)   Employee6 (13)
"""

class EmployeeSystem:
    def __init__(self, data: {}):
        self.data = data

    def get_leaders(self, id: int):
        res = set()

        def backtrack(curr_id):
            if curr_id == id:
                return True

            for next_id in self.data.get(curr_id, {}):
                backtrack(next_id)

        backtrack(1, set())

        return res

    def find_commend_leaders(self, id1:int, id2:int):
        leaders_set_1 = self.get_leaders(id1)

        return []
