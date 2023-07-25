import sys
import string

tok_eof = -1
tok_def = -2
tok_extern = -3
tok_identifier = -4
tok_number = -5
tok_print = -6

IdentifierStr = ""
NumVal = 0.0


def gettok():
    global IdentifierStr
    global NumVal

    LastChar = ' '

    while LastChar.isspace():
        LastChar = sys.stdin.read(1)
        # print("HERE IS WHITERPASCVEAR:", LastChar)
        # print("HERE IS VAL:", NumVal)

    if LastChar.isalpha():
        IdentifierStr = LastChar
        LastChar = sys.stdin.read(1)
        while LastChar.isalnum():
            IdentifierStr += LastChar
            LastChar = sys.stdin.read(1)

        if IdentifierStr == "def":
            return tok_def
        if IdentifierStr == "print" or IdentifierStr == "disp":
            return tok_print

        # Add other keywords here

        return tok_identifier

    if LastChar.isdigit() or LastChar == '.':
        foundDot = LastChar == '.'
        NumStr = ""

        while LastChar.isdigit() or LastChar == '.':
            NumStr += LastChar
            LastChar = sys.stdin.read(1)

            if LastChar == '.':
                if foundDot:
                    sys.stderr.write("Abort during lexing: found number with at least two decimal points\n")
                    sys.exit(1)
                else:
                    foundDot = True
                    continue

        if NumStr == ".":
            sys.stderr.write("Abort during lexing: found invalid number \".\"\n")
            sys.exit(1)

        NumVal = float(NumStr)
        return tok_number

    if LastChar == '#':
        while LastChar != '\n' and LastChar != '\r':
            LastChar = sys.stdin.read(1)

        if LastChar != '\n':
            return gettok()

    if LastChar == '':
        return tok_eof

    ThisChar = LastChar
    LastChar = sys.stdin.read(1)
    return ord(ThisChar)


def main():
    while True:
        token = gettok()
        if token == tok_eof:
            break
        print(token)


if __name__ == "__main__":
    main()