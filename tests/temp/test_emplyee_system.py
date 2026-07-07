from app.temp.emplyee_system import EmployeeSystem

data = {
    1: {"id":1, "role": "ceo", "reports": [2, 5]},
    2: {"id":2, "role": "director", "reports": [3, 4]},
    3: {"id":3, "role": "manager", "reports": [8, 9]},
    4: {"id":4, "role": "manager", "reports": [10, 11]},
    5: {"id":5, "role": "director", "reports": [6, 7]},
    6: {"id":6, "role": "manager", "reports": [12, 13]},
    7: {"id":7, "role": "manager", "reports": []},
    8: {"id":8, "role": "employee", "reports": []},
    9: {"id":9, "role": "employee", "reports": []},
    10: {"id":10, "role": "employee", "reports": []},
    11: {"id":11, "role": "employee", "reports": []},
    12: {"id":12, "role": "employee", "reports": []},
    13: {"id":13, "role": "employee", "reports": []},
}

solver = EmployeeSystem(data)


def test_common_leaders_same_manager():
    assert solver.find_commend_leaders(8, 9) == [3, 2, 1]


def test_common_leaders_cross_director():
    assert solver.find_commend_leaders(8, 12) == [1]


def test_common_leaders_same_employee():
    assert solver.find_commend_leaders(12, 12) == [6, 5, 1]


def test_common_leaders_with_unknown_employee():
    assert solver.find_commend_leaders(8, 999) == []
