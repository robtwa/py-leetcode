import pytest

from app.linked_list_cycle_141 import Solution, ListNode

solver = Solution()

def test_1():
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next

    assert solver.hasCycle(head) == True

def test_2():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head

    assert solver.hasCycle(head) == True

def test_3():
    head = ListNode(1)

    assert solver.hasCycle(head) == False
