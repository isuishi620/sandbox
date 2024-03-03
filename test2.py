from typing import List


def calc_sum(numbers: List[int]) -> int:
    sum = 0
    for number in numbers:
        sum += number
    return sum


result = calc_sum([1, 3, 3])  # mypyはこの行で型の不一致を指摘するはずです

print("The sum is:", result)

unused_var = 5  # flake8は未使用の変数を指摘するはずです
