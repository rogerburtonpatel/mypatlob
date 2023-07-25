class Block:
    def __init__(self, my_header, my_depth, my_parent):
        self.parent = my_parent
        self.header = my_header
        self.content = []
        self.depth = my_depth
        self.assigned_namespace = {}

class Line:
    def __init__(self, my_text):
        self.text = my_text
        self.type = 

class LineType(Enum):
    ASSGN = 1
    FOR = 2
    WHILE = 3
    IF = 4
    ELIF = 5
    ELSE = 6
    DEF = 7
    RETURN = 8
    TRY = 9
    CATCH = 10
    CONT = 11
    BREAK = 12
    EXPR = 13


def line_parse(line):
    name = "[a-zA-Z][a-zA-Z_\d]*"
    number = "\d+\.*\d*"
    array = "[]" #????
    binop_expr = "expression binop expression"
    unop_expr = "unop expression"

    literal = "number | string | array"
    function_call = "name\(args\)"
    indexing = "array[expression]"
    expression = "literal | name | function_call |  binop_expr | unop_expr | indexing | \(expression\)"
    assignment = "var = expression"
    for_loop = "for variable in expression:"
    while_loop = "while expression:"
    if_block = "if expression:"
    else_block = "else:"
    elif_block = "elif expression:"
    ret = "return expression"

    args = "'' | expression | (expression, args)"
    name_list = "'' | name | (name, name_list)"
    function = "def name\(name_list*\)"

class Name:
    def __init__(self, txt):
        self.text = txt

    def to_string(self):
        return self.text

import re

class Name:
    def __init__(self, txt):
        self.text = txt

    def to_string(self):
        return self.text


class Number:
    def __init__(self, txt):
        self.text = txt

    def to_string(self):
        return self.text


class Array:
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def to_string(self):
        return f"[{', '.join(map(str, self.elements))}]"


class BinOpExpression:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def to_string(self):
        return f"({self.left} {self.operator} {self.right})"


class UnOpExpression:
    def __init__(self, operator, expression):
        self.operator = operator
        self.expression = expression

    def to_string(self):
        return f"{self.operator}{self.expression}"


class Literal:
    def __init__(self, txt):
        self.text = txt

    def to_string(self):
        return self.text


class FunctionCall:
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def to_string(self):
        return f"{self.name}({', '.join(map(str, self.args))})"


class Indexing:
    def __init__(self, array, expression):
        self.array = array
        self.expression = expression

    def to_string(self):
        return f"{self.array}[{self.expression}]"


class Assignment:
    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression

    def to_string(self):
        return f"{self.variable} = {self.expression}"


class ForLoop:
    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression

    def to_string(self):
        return f"for {self.variable} in {self.expression}:"


class WhileLoop:
    def __init__(self, expression):
        self.expression = expression

    def to_string(self):
        return f"while {self.expression}:"


class IfBlock:
    def __init__(self, expression):
        self.expression = expression

    def to_string(self):
        return f"if {self.expression}:"


class ElseBlock:
    def __init__(self):
        pass

    def to_string(self):
        return "else:"


class ElifBlock:
    def __init__(self, expression):
        self.expression = expression

    def to_string(self):
        return f"elif {self.expression}:"

class Ret:
    def __init__(self, expression):
        self.expression = expression

    def to_string(self):
        return f"return {self.expression}:"