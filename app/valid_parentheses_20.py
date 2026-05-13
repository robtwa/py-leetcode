"""
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []
        for curr_char in s:
            # Check if the current char is a close bracket
            if curr_char in bracket_dict:
                if len(stack) == 0:
                    # Stack is empty
                    return False
                else:
                    prev_str = stack.pop()
                    if prev_str != bracket_dict[curr_char]:
                        return False
            else:
                stack.append(curr_char)

        return True
