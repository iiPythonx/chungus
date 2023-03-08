# Copyright 2023 iiPython

# Modules
from types import FunctionType
from typing import List

# Base classes
class Node(object):
    def __init__(self, lexical: str, calculate: FunctionType) -> None:
        self.lexical = lexical
        self.calculate = calculate

    def __str__(self) -> str:
        return self.lexical

TT_TYPES = {
    n.lexical: n
    for n in [
        Node("+", lambda x, y: x + y),
        Node("-", lambda x, y: x - y),
        Node("*", lambda x, y: x * y),
        Node("/", lambda x, y: x / y),
        Node("^", lambda x, y: x ** y)
    ]
}

# Operation class
class Operation(object):
    def __init__(self, left: int | float, right: int | float, node: Node) -> None:
        self.value = node.calculate(
            left if not isinstance(left, Operation) else left.value,
            right if not isinstance(right, Operation) else right.value
        )

    def __int__(self) -> int:
        return self.value

    def __repr__(self) -> str:
        return str(self.value)

# Parser
def parse(expression: str) -> List[Operation]:
    return "nothing yet"

# Testing
print(parse("2*(3^(2-5))"))
print(Operation(2, Operation(3, Operation(2, 5, TT_TYPES["-"]), TT_TYPES["^"]), TT_TYPES["*"]))
