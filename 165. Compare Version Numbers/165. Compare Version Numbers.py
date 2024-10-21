from typing import List
from itertools import zip_longest

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))
        for rev1, rev2 in zip_longest(v1, v2, fillvalue=0):
            if rev1 > rev2:
                return 1
            elif rev1 < rev2:
                return -1
        return 0
