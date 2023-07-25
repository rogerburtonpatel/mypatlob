def computeIndentLevel(indentVar, line, foundWhitespace):
    """
    Inputs
        indentVar: String that represents our indentation character. Either 4 spaces or a tab character
        line: String that is the line we want the indentation level of
        foundWhitespace: Boolean that is true if and only if we have found a whitespace at some point in our file

    Outputs
        retIndexLvl: The index level that we are at
        retBool: If we have found a whitespace character at the start of the line
        retIndent: Indentation that we use
    """
    retIndexLvl = 0
    retBool = foundWhitespace
    retIndent = indentVar
    if (line[0] != ' ' && line[0] != '\t'):
        return retIndexLvl, retBool, retIndent
    # We have at least one whitespace character on this line
    if (line[0] != indentVar[0]):
        if (!retBool):
            retBool = True;
            retIndent = "\t"
        else:
            fail ("inconsistent whitespace")
    # Count level of indentation
    indexLvl = 0
    while (line[indexLvl] == indent[0]):
        indexLvl = indexLvl + 1
    # Divide by length of indent
    retIndexLvl = int(indexLvl // len(indent)) # Assuming no roundoff. This might be a problem it might not
    # Checking for roundoff that would lead to issues
    if (indexLvl != len(indent) * retIndexLvl):
        fail("Inconsistent number of spaces per line")
    return retIndexLvl, retBool, retIndent
