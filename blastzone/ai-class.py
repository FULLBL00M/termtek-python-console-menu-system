class ConsoleMenu:
    class ConsoleMenuOption:
        def __init__(self, key, label, func):
            self.key = key
            self.label = label
            self.func = func

        def get_key(self):
            return self.key

        def set_key(self, key):
            self.key = key

        def get_label(self):
            return self.labelchi

        def set_label(self, label):
            self.label = label

        def get_func(self):
            return self.func

        def set_func(self, func):
            self.func = func

    def __init__(self, banner, menu_options=None, previous_menu=None):
        self.banner = banner
        self.menu_options = menu_options or []
        self.previous_menu = previous_menu
        self.menu_name = None

    def go_back(self):
        self.previous_menu.show_full()

    def get_banner(self):
        return self.banner

    def set_banner(self, banner):
        self.banner = banner

    def get_menu_options(self):
        return self.menu_options

    def set_menu_options(self, menu_options):
        self.menu_options = menu_options

    def get_previous_menu(self):
        return self.previous_menu

    def set_previous_menu(self, previous_menu):
        self.previous_menu = previous_menu

    def set_menu_name(self, menu_name):
        self.menu_name = menu_name

    def get_menu_name(self):
        return self.menu_name

    def show_banner(self):
        print(f"\n{self.banner}\n")

    def show_menu_options(self):
        if self.menu_options is not None:
            for option in self.menu_options:
                print(f"[ {option.key} ]: {option.label}")
            print()

    def show_previous_menu(self):
        if self.previous_menu is not None:
            print(self.previous_menu)

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
            selected_option = next(
                (x for x in self.menu_options if x.key == choice), None)

            # if a matching option was found, perform the corresponding action
            if selected_option is not None:
                print()
                selected_option.func()
            # if no matching option was found, exit the main loop
            else:
                print("Invalid selection. Please try again.")
                self.show_full()
