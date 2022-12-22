import os

class ConsoleMenuOption:
  def __init__(self, key, label, func):
    self.key = key
    self.label = label
    self.func = func

class ConsoleMenu:
  def __init__(self, banner, menu_options=None, previous_menu=None):
    self.banner = banner
    self.menu_options = menu_options
    self.previous_menu = previous_menu

  def show_banner(self):
    print(f"\n{self.banner}\n")

  def show_menu_options(self):
    for option in self.menu_options:
      print(f"[ {option.key} ]: {option.label}")
    print()

  def show_previous_menu(self):
    if self.previous_menu is not None:
      print(self.previous_menu)
    else:
      print("NONE~!")

  def show_full(self):
      """
      Shows the full menu and returns the user's selection.
      """
      while True:
          print(f"\n{self.banner}\n")
          for option in self.menu_options:
              print(f"[ {option.key} ]: {option.label}")
          print()
          choice = input("Enter your choice: ")

          # find the menu option with the matching key
          selected_option = next((x for x in self.menu_options if x.key == choice), None)

          # if a matching option was found, perform the corresponding action
          if selected_option is not None:
              print()
              selected_option.func()
          # if no matching option was found, exit the main loop
          else:
              print("Invalid selection. Please try again.")
              self.show_full()

"""
************************************************************************************************************************************
"""

def clear():
    os.system("cls" if os.name == "nt" else "clear")

"""
************************************************************************************************************************************
"""

def print_columns(data, keys, max_width=30):
  print()
  # Calculate the width of each column
  column_widths = {}
  for key in keys:
    column_widths[key] = max(max_width, max([len(str(row[key])) for row in data]))
  
  # Print the column names
  row_str = ''
  for key in keys:
    key_str = str(format_simple_heading_spaced(key))[:column_widths[key]]
    row_str += f"{key_str}{' '*(column_widths[key]-len(key_str))}\t"
  print(row_str)
  
  # Print the rows of data
  for row in data:
    row_str = ''
    for key in keys:
      value_str = str(row[key])[:column_widths[key]]
      row_str += f"{value_str}{' '*(column_widths[key]-len(value_str))}\t"
    print(row_str)
  print()


"""
************************************************************************************************************************************
"""

def format_simple_heading_spaced(text):
  """
  Format the given text by adding brackets, padding characters, and separating each letter with a space.
  
  Parameters:
  text (str): The text to format.
  
  Returns:
  str: The formatted text.
  """
  # Separate each letter in the text with a space
  spaced_text = ' '.join(list(text))
  
  # Add the brackets and padding characters
  formatted_text = f"[  {spaced_text}  ]"
  
  return formatted_text
