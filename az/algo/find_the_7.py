# In a list of numbers, assume 0 through 100, we want to return all the numbers, in the same order
# But, when we encounter a number divisible by 7 or has the number 7 in it, we want to return the word "boom".
# eg: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# would become: [1, 2, 3, 4, 5, 6, "boom", 8, 9, 10, 11, 12, 13, "boom", 15, 16, "boom", 18, 19]
from typing import Iterable


def find_the_sevens(nums: Iterable[int]) -> Iterable[str]:
    """non functional way"""
    results = []
    for num in nums:
        if is_divisible_7(num) or does_seven_exist(num):
            results.append("boom")
        else:
            results.append(num)
    return results


def is_divisible_7(num: int) -> bool:
    return num % 7 == 0


def does_seven_exist(num: int) -> bool:
    if True in [char == "7" for char in str(num)]:
        return True
    return False


def find_the_sevens2(nums: Iterable[int]) -> Iterable[str]:
    """comprehension version"""
    return [
        str(num) if not (is_divisible_7(num) or does_seven_exist(num)) else "boom"
        for num in nums
    ]

print(
    find_the_sevens2(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    )
)
