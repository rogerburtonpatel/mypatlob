class Block:
    def __init__(self, my_header, my_depth, my_parent):
        self.parent = my_parent
        self.header = my_header
        self.content = []
        self.depth = my_depth
        self.assigned_namespace = {}

    def to_string()
        pass
    def appendContent(newLine):
        self.content.append(newLine)

def parse_file(file_name):

    with open(file_name) as f:
        text = f.read()
    # Create a new Block that will serve as a sentinal node in our Tree
    rootBlock = Block(None, None, None);
    lines = text.split("\n")
    #indent = "    |\t"
    foundWhiteSpace = False
    # Initially assume that the user used 4 spaces. If we find a tab we set above to true and reassign indent
    indent = "    "
    # We start at 0 and once we reach a new Block we increment
    indentLevel = 0
    # Flag that determines if we want to create a new Block
    newBlock = True
    for line in lines:
        # line is a string. So we need to determine first if we are in a new block
        # This happens when we reach a new structured object like
        knownExpressions = ["if ", "elif ", "else ", "while ", "for ", "def ", "try ", "catch "]
        # if, elif, else, while, for, def, try, catch
        if (line[0] == ' ' || line[0] == '\t'):
            if (newBlock):
                newBlock = False
                # Check for the indent character
                if(line[0] != indent[0]):
                    if (foundWhiteSpace):
                        fail("White space mismatch")
                    else:
                        # This only happens when indent = '    ' and line[0] = '\t'
                        indent = '\t'
                        foundWhiteSpace = True
            else:
                fail("Unexpected whitespace")
        else:
            # Now we need to check if we are going into a new block on the next iteration
            for (expression in knownExpressions):
                if (expression == line[0:len(expression)]):
                    # Then we want to go to a new indentation level
                    indentLevel = indentLevel + 1
            # Now, we read in our line and either create a new
