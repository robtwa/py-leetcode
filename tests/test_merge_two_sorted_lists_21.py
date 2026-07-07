import pytest

from app.merge_two_sorted_lists_21 import Solution, ListNode

solver = Solution()

def build_list(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def listnode_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def test_1():
    list1 = build_list([1, 2, 4])
    list2 = build_list([1, 3, 4])
    expected = [1, 1, 2, 3, 4, 4]

    result = solver.mergeTwoLists(list1, list2)
    print(result)

    assert listnode_to_list(result) == expected


def test_2():
    list1 = build_list([])
    list2 = build_list([])
    expected = []

    result = solver.mergeTwoLists(list1, list2)

    assert listnode_to_list(result) == expected


def test_3():
    list1 = build_list([])
    list2 = build_list([0])
    expected = [0]

    result = solver.mergeTwoLists(list1, list2)

    assert listnode_to_list(result) == expected

