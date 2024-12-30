# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

pairs = [(5, "apple"), (2, "banana"), (9, "cherry")]

class Solution:
    # Implementation of Insertion Sort
    def insertionSort(self, pairs: list[Pair]) -> list[list[Pair]]:
        n = len(pairs)
        res = []  # To store the intermediate states of the array

        for i in range(n):
            j = i - 1

            # Move elements that are greater than key one position ahead
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1

            # Clone and save the entire state of the array at this point
            res.append(pairs[:])

        return res