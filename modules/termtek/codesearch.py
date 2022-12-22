import os
from termtek import colorize as cz
from termtek import consolemenu as cm
"""
************************************************************************************************************************************
"""

def get_function_name(code):
    """
    Extract function name from a line beginning with "def "
    """
    assert code.startswith("def ")
    return code[len("def "): code.index("(")]

"""
************************************************************************************************************************************
"""

def get_until_no_space(all_lines, i) -> str:
    """
    Get all lines until a line outside the function definition is found.
    """
    ret = [all_lines[i]]
    for j in range(i + 1, i + 10000):
        if j < len(all_lines):
            if len(all_lines[j]) == 0 or all_lines[j][0] in [" ", "\t", ")"]:
                ret.append(all_lines[j])
            else:
                break
    return "\n".join(ret)

"""
************************************************************************************************************************************
"""

def enumerate_functions(filepath):
    """
    Get all functions in a Python file.
    """
    whole_code = open(filepath).read().replace("\r", "\n")
    all_lines = whole_code.split("\n")
    counter = 0
    for i, l in enumerate(all_lines):
        if l.startswith("def "):
            counter += 1
            code = get_until_no_space(all_lines, i)
            function_name = get_function_name(code)
            # Get the filename from the filepath
            filename = os.path.basename(filepath)
            yield {
                "id": f"{filename}-{counter}",  # append the filename to the id
                "code": code, 
                "function_name": function_name, 
                "filepath": filepath,
                "line_number": i+1  # add the line number
            }

"""
************************************************************************************************************************************
"""

def print_all_function_names(all_funcs):
    print(cz.colorize(cm.format_simple_heading_spaced("All Function Names"), "green"))
    max_length = 0
    for i in range(len(all_funcs)):
        if len(all_funcs[i]['function_name']) > max_length:
            max_length = len(all_funcs[i]['function_name'])
    for i in range(len(all_funcs)):
        print(f"{all_funcs[i]['function_name']}{' '*(max_length-len(all_funcs[i]['function_name']))}\t{all_funcs[i]['filepath']}")
    print("\n")

"""
************************************************************************************************************************************
"""