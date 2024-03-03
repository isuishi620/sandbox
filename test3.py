import json  # noqa: F401
from typing import List


def example_function(numbers: List[int]) -> int:
    sum = 0  # 故意に不適切なスペースを使用
    for number in numbers:
        sum += number  # `black`によってインデントが修正されるべき
    return sum


result = example_function([1, "2", 3])  # type: ignore

print("Result:", result)

unused_var = 5  # `autoflake`がこの未使用の変数を削除する


# `flake8`は上記の問題（未使用のインポート、不適切なインデント、等）を指摘する
