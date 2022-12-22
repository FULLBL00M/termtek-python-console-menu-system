font = {}

font['a'] = ['▄▀█',
             '█▀█']

font['b'] = ['█▄▄',
             '█▄█']

font['c'] = ['█▀▀',
             '█▄▄']

font['d'] = ['█▀▄',
             '█▄▀']

font['e'] = ['█▀▀',
             '██▄']

font['f'] = ['█▀▀',
             '█▀░']

font['g'] = ['█▀▀',
             '█▄█']

font['h'] = ['█░█',
             '█▀█']

font['i'] = ['█',
             '█']

font['j'] = ['░░█',
             '█▄█']

font['k'] = ['█▄▀',
             '█░█']

font['l'] = ['█░░',
             '█▄▄']

font['m'] = ['█▀▄▀█',
             '█░▀░█']

font['n'] = ['█▄░█',
             '█░▀█']

font['o'] = ['█▀█',
             '█▄█']

font['p'] = ['█▀█',
             '█▀▀']

font['q'] = ['█▀█',
             '▀▀█']

font['r'] = ['█▀█',
             '█▀▄']

font['s'] = ['█▀',
             '▄█']

font['t'] = ['▀█▀',
             '░█░']

font['u'] = ['█░█',
             '█▄█']

font['v'] = ['█░█',
             '▀▄▀']

font['w'] = ['█░█░█',
             '▀▄▀▄▀']

font['x'] = ['▀▄▀',
             '█░█']

font['y'] = ['█▄█',
             '░█░']

font['z'] = ['▀█',
             '█▄']

font[' '] = ['  ',
             '  ']

font['\''] = ['▀',
              '░']

font['-'] = ['▄▄',
             '░░']

font['_'] = ['▄▄',
             '░░']

font['"'] = ['█░█',
             '░░░']

font['!'] = ['█',
             '▄']

font['.'] = ['░',
             '▄']

font['['] = ['█▀',
             '█▄']

font[']'] = ['▀█',
             '▄█']

# Don't access this funtion directly, use build_fancy_font instead
def return_fancy_font(line_chars: list[list[str]], spacing: str):
    lines = []
    for line_i in range(max([len(x) for x in line_chars])):
        line = []
        for char in line_chars:
            if len(char) > line_i:
                line.append(char[line_i])
        lines.append(spacing.join(line))
    return '\n'.join(lines)

# This function is used to build a fancy font from a string
# Example Usage:
"""
os.system("clear")
banner = ttk.build_fancy_font("[ bloomy's debugging sketch ]")
print(f"\n{banner}\n")
"""
def build_fancy_font(line: str):
    # Initialize an empty list to store the font characters
    line_chars = []

    # Iterate through each character in the line
    for c in line.lower():
        # If the character is in the font dictionary, add it to the list
        if c in font:
            line_chars.append(font[c])
        # If the character is not in the font dictionary, use a default value instead
        else:
            line_chars.append('')

    # Return the fancy font using the modified list of characters
    return return_fancy_font(line_chars, ' ')