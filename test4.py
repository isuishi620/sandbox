# import os  # 複数のインポートが同じ行にある
# import sys  # 未使用のインポート


def calculate_sum(numbers):
    sum = 0  # 'sum'は組み込み関数を覆い隠す
    for number in numbers:
        sum += number
    return sum


def greet(name: str, age: int) -> str:
    return f"Hello, {name}. You are {age} years old."


result = calculate_sum([1, 2, 3, 4])
print("Sum:", result)

greeting = greet("Alice", 30)  # 'age'パラメータに文字列を渡している

unused_variable = "This is not used anywhere"


def another_function():
    pass  # 不要なパスステートメント


class MyClass:
    def method(self):
        pass  # こちらも不要なパスステートメント
