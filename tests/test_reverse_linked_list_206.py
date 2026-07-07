import pytest

from app.reverse_linked_list_206 import Solution, ListNode

solver = Solution()

def test_1():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = solver.reverseList(head)

    assert res.val == 5
    assert res.next.val == 4
    assert res.next.next.val == 3
    assert res.next.next.next.val == 2
    assert res.next.next.next.next.val == 1
    assert res.next.next.next.next.next is None

def test_2():
    head = ListNode(1, ListNode(2))
    res = solver.reverseList(head)

    assert res.val == 2
    assert res.next.val == 1
    assert res.next.next is None

def test_3():
    head = None
    res = solver.reverseList(head)

    assert res is None
