
from typing import List

"""
To create an integer array, S, the following operation is performed exactly m times. Sis initially empty.
    • Choose any values[i] that is available, that is, where state[i] = 'T, the same element can be chosen any
      number of times.
    • Append the value in values[i] to S.
    • For all state[i] = 'O' such that state[i-1] = '1', change statel[i] to '1':
      For example, if state = '0100101', it should equal '0110111' after the operation.
"""
class Solution:
    """
    I first convert the `state` string into a list so it can be modified easily.

    Here:
    * `'1'` means the position is available
    * `'0'` means it is currently locked

    Then I perform at most `m` selection rounds.

    In each round, I scan the entire `values` array and find the largest number whose corresponding state is '1'.
    I then add that value to the result list.

    After selecting a number, I update the state.
    If a position is currently `'0'` but its left neighbor is `'1'`, that position becomes unlocked and changes to '1'.

    As the algorithm continues, more positions gradually become available for future selections.
    """
    def getOptimalSequence(self, values, state, m) -> List[int]:
        res = []
        state_list = list(state)

        # Find m numbers
        for k in range(m):
            # Find the largest value
            num = -999
            for i in range (len(values)):
                if state_list[i] == '1' and values[i] > num:
                    num = values[i]

            if num == -999:
                break;

            res.append(num)

            # Change all qualified state from 0 to 1
            for j in range(1, len(state_list)):
                if state_list[j] == '0' and state_list[j-1] == '1':
                    state_list[j] = '1'

        return res
