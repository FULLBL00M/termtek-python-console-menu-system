def colorize(string, color):
    """
    Colorize a string for the terminal.
    
    Args:
        string (str): The string to colorize.
        color (str): The color to use. Valid options are:
            'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'
    
    Returns:
        str: The colorized string.
    """
    # Define the escape sequences for the different colors
    colors = {
        "red": "\033[1;31m",
        "green": "\033[1;32m",
        "yellow": "\033[1;33m",
        "blue": "\033[1;34m",
        "magenta": "\033[1;35m",
        "cyan": "\033[1;36m",
        "white": "\033[1;37m",
    }
    
    # Check if the specified color is valid
    if color not in colors:
        raise ValueError(f"Invalid color: {color}")
    
    # Return the colorized string
    return f"{colors[color]}{string}\033[0m"