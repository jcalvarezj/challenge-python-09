from typing import List


class Solution:
    def duplicate_zeros(self, arr: List[int]):
        initial_size = len(arr)
        arr_enum = enumerate(arr.copy())
        acumulate = 0
        for i, num in arr_enum:
            if num == 0:
                arr.insert(i + acumulate + 1, 0)
                acumulate += 1
        for i in range(len(arr) - initial_size):
            arr.pop()