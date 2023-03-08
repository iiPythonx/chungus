# Copyright 2023 iiPython

# Base classes
class TokenTypes:
    TOK_ADD = "+"
    TOK_SUB = "-"
    TOK_MUL = "*"
    TOK_DIV = "/"
    TOK_POW = "^"

class Operation(object):
    def __init__(self) -> None:
        pass

# Parser
def parse(expression: str) -> List[Operation]:
    return "debug"

# Testing
print(parse("2*(3^(2-5))"))
