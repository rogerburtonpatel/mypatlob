class Block:
    def __init__(self, my_header, my_depth, my_parent):
        self.parent = my_parent
        self.header = my_header
        self.content = []
        self.depth = my_depth
        self.assigned_namespace = {}

    def to_string()
        pass

def parse_file(file_name):
    f = open(file_name)
    text = f.read()
    f.close()

    lines = text.split("\n")
    indent = "    |\t"

    program = Block
