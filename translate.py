import re
from enum import Enum

class Name(Enum):
    VAR = 1
    FUNC = 2

def computeIndentLevel(indentVar, line):
    """
    Inputs
        indentVar: String that represents our indentation character. Either 4 spaces or a tab character
        line: String that is the line we want the indentation level of

    Outputs
        retIndexLvl: The index level that we are at
    """
    retIndexLvl = 0
    retIndent = indentVar
    if (line[0] != ' ' and line[0] != '\t'):
        return retIndexLvl
    # We have at least one whitespace character on this line
    if (line[0] != indentVar[0]):
        fail ("inconsistent whitespace")
    # Count level of indentation
    indexLvl = 0
    while indexLvl < len(line) and (line[indexLvl] == indentVar[0]):
        indexLvl = indexLvl + 1
    # Divide by length of indent
    retIndexLvl = int(indexLvl // len(indentVar)) # Assuming no roundoff. This might be a problem it might not
    
    # Checking for roundoff that would lead to issues
    if (indexLvl != len(indentVar) * retIndexLvl):
        fail("Inconsistent number of spaces per line")
    return retIndexLvl

def isWhiteSpace(char):
    return char == " " or char == "\t"

def skip_end(line):
    trimmed_line = line.strip()
    return trimmed_line[:5] == "else:" or trimmed_line[:5] == "elif "

def translate(file_name):
    f = open(file_name)
    text = f.read()
    f.close()

    f = open("matlab.m", "w")
    lines = text.split("\n")
    indent_mode = None

    namespace = {}
    prev_depth = 0

    for line in lines:
        if not line or str.isspace(line):
            continue

        newline = line
        # count indents
        if indent_mode == None and isWhiteSpace(line[0]):
            indent_mode = " "*4 if line[0] == " " else "\t"
        my_depth = computeIndentLevel(indent_mode, line)
        gap = prev_depth - my_depth if not skip_end(line) else prev_depth - my_depth - 1
        if gap > 0:
            for _ in range(gap):
                f.write("end\n")
        prev_depth = my_depth


        # match expressions
        semicolon = True

        # assignment
        assgn = re.compile(r"(?P<name>\w(\w|\_)*)\s*=", re.VERBOSE)
        assgn_match = assgn.search(newline)
        if assgn_match != None:
            my_name = assgn_match['name']
            namespace[assgn_match['name']] = (Name.VAR, my_name)

        # for
        forloop = re.compile(r"for\s+(?P<name>\w(\w|\_|\d)*)\s+in\s+(?P<iter>.*):", re.VERBOSE)
        forloop_match = forloop.search(newline)
        if forloop_match != None:
            my_name = forloop_match['name']
            namespace[forloop_match['name']] = (Name.VAR, my_name)
            newline = f"for {my_name} = {forloop_match['iter']}"
            semicolon = False

        # if/else
        elseif = re.compile(r"elif\s+(?P<cond>.*):", re.VERBOSE)
        elseif_match = elseif.search(newline)
        if elseif_match != None:
            newline = f"elseif {elseif_match['cond']}"
            semicolon = False
        else:
            ifif = re.compile(r"if\s+(?P<cond>.*):", re.VERBOSE)
            ifif_match = ifif.search(newline)
            if ifif_match != None:
                newline = f"if {ifif_match['cond']}"
                semicolon = False

        elseelse = re.compile(r"else:", re.VERBOSE)
        elseelse_match = elseelse.search(newline)
        if elseelse_match != None:
            newline = "else"
            semicolon = False

        # while
        whileloop = re.compile(r"while\s+(?P<iter>.*):", re.VERBOSE)
        whileloop_match = whileloop.search(newline)
        if whileloop_match != None:
            newline = f"while {whileloop_match['iter']}"
            semicolon = False

        # function def
        func = re.compile(r"def\s+(?P<name>\w(\w|\_|\d)*)\((?P<args>.*)\):", re.VERBOSE)
        func_match = func.search(newline)
        if func_match != None:
            new_name = func_match['name']
            namespace[func_match['name']] = (Name.FUNC, new_name)
            newline = f"function {new_name}({func_match['args']})"
            semicolon = False

        # range
        rangere = re.compile(r"[^a-zA-Z_]range\(\s*(?P<start>[^,]+)(,\s*(?P<stop>[^,]+))?(,\s*(?P<step>[^,]+))?\)", re.VERBOSE)
        for rangere_match in rangere.finditer(newline):
            start, end = rangere_match.span()
            if rangere_match["step"] != None:
                newline = f"{newline[:start+1]}{rangere_match['start']}:{rangere_match['step']}:{rangere_match['stop']}{newline[end:]}"
            elif rangere_match["stop"] != None:
                newline = f"{newline[:start+1]}{rangere_match['start']}:{rangere_match['stop']}{newline[end:]}"
            else:
                newline = f"{newline[:start+1]}1:{rangere_match['start']}{newline[end:]}"

        # indexing arr[1] (and + 1 to index)
        index = re.compile(r"(\w|\_|\d)\[(?P<ind>.+?)\]", re.VERBOSE)
        for index_match in index.finditer(newline):
            newline = newline.replace("[" + index_match['ind'] + "]",  "(" + index_match['ind'] + " + 1)")

        # f.write -> disp
        disp = re.compile(r"f.write(ln)?\((?P<str>.*)\)", re.VERBOSE)
        disp_match = disp.search(newline)
        if disp_match != None:
            newline = f"disp({disp_match['str']})"
            semicolon = False

        # ** -> ^
        newline = newline.replace("**", "^")

        # != -> ~=
        newline = newline.replace("!=", "~=")

        # comments
        newline = newline.replace("#", "%")

        if semicolon:
            newline = newline + ";"
        f.write(newline+"\n")

    for _ in range(prev_depth):
        f.write("end\n")
    f.close()

translate("test.txt")

