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
    literal = "number | string | array"
    expression = "literal | variable | function_call | bin_op | (expression)"
    assignment = "var = expression"
    for_loop = "for variable in expression:"
    while_loop = "while expression:"
    if_block = "if expression:"
    else_block = "else:"
    elif_block = "elif expression:"

    args = "arg | arg, args"
    function = "def name(args)"
