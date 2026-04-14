
from typing import List

class Solution:
    def getOptimalSequence(self, values, state, m) -> List[int]:
        n = len(values)
        s = list(state)
        res = []

        for _ in range(m):
            # 找当前可选中的最大值
            max_val = -1
            for i in range(n):
                if s[i] == '1':
                    max_val = max(max_val, values[i])

            if max_val == -1:
                break

            res.append(max_val)

            # ⃣ unlock
            for i in range(1, n):
                if s[i] == '0' and s[i - 1] == '1':
                    s[i] = '1'

            ## this causes bug
            # prev = s.copy()
            # for i in range(1, n):
            #     if prev[i] == '0' and prev[i - 1] == '1':
            #         s[i] = '1'

        return res