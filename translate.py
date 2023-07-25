import re

def translate(file_name):
    f = open(file_name)
    text = f.read()
    f.close()

    f.open("matlab.m")

    lines = text.split("\n")
    indent = "    |\t"

    namespace = {}
    prev_depth = 0

    for line in lines:
        # count indents


        # match expressions
        assgn = re.compile('(?P<var> )\s*=\')

        # for

        # if/else

        # while

        # function def

        # range

        # indexing arr[1] (and + 1 to index)

        # print -> disp

        # ** -> ^

        # != -> ~=

        # 


        
        
        



