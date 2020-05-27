"""
This module includes my solution to the challenge
"""
from typing import List


class Solution:
    """
    This class represents a solution object that provides methods used to
    compute a result
    """
    def duplicate_zeros(self, arr: List[int]):
        """
        This method duplicates the zeros inside the input array, while
        respecting its original size
        """
        initial_size = len(arr)
        arr_enum = enumerate(arr.copy())
        acumulate = 0
        for i, num in arr_enum:
            if num == 0:
                arr.insert(i + acumulate + 1, 0)
                acumulate += 1
        for i in range(len(arr) - initial_size):
            arr.pop()
