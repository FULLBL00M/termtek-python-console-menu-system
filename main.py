import modules.termtek as ttk
import sys

# Put your functions here
# or import them from another file

def testone():
    print(ttk.colorize(ttk.build_fancy_font("Test one"), "red"))
    print()

def testtwo():
    print(ttk.colorize(ttk.build_fancy_font("Test two"), "blue"))
    print()

def settings_testone():
    print(ttk.colorize(ttk.build_fancy_font("Settings Test one"), "green"))
    print()

def settings_testtwo():
    print(ttk.colorize(ttk.build_fancy_font("Settings Test two"), "yellow"))
    print()

def exit():
    bye_felisha = ttk.colorize(ttk.return_simple_heading_spaced("GOODBYE"), "green")
    ttk.print_text_humanistic(bye_felisha)
    print()
    sys.exit()

# ======================================================================================

# Put your menus here

all_menus = []

root_menu = {
    "menu_name": "root_menu",
    "banner": ttk.build_fancy_font("Main Menu"),
    "menu_options": [
        ["test1", "Test function one", testone],
        ["test2", "Test funtion two", testtwo],
        ["openai", "Play with Openai API", {"goto": "openai_api_menu"}],
        ["settings", "Change settings for the program", {"goto": "settings_menu"}],
        ["exit", "Exit the program", exit]
    ]
}
all_menus.append(root_menu)

openai_api_menu = {
    "menu_name": "openai_api_menu",
    "banner": ttk.build_fancy_font("Openai Api Menu"),
    "menu_options": [
        ["test1", "Test openai function one", testone],
        ["test2", "Test openai funtion two", testtwo],
        ["aisettings", "Change settings for openai", {"goto": "openai_api_settings_menu"}]
    ]
}
all_menus.append(openai_api_menu)

settings_menu = {
    "menu_name": "settings_menu",
    "banner": ttk.build_fancy_font("Settings Menu"),
    "menu_options": [
        ["password", "Change your account password", settings_testone],
        ["email", "Change your account email", settings_testtwo]
    ]
}
all_menus.append(settings_menu)

openai_api_settings_menu = {
    "menu_name": "openai_api_settings_menu",
    "banner": ttk.build_fancy_font("Openai Api Settings Menu"),
    "menu_options": [
        ["test1", "Test openai settings function one", settings_testone],
        ["test2", "Test openai settings funtion two", settings_testtwo]
    ]
}
all_menus.append(openai_api_settings_menu)

# ======================================================================================

if __name__ == "__main__":
    ttk.build_console_menu_objects(all_menus)
    for menu in all_menus:
        if menu["menu_name"] == "root_menu": # <====== This is the only change you might need to make but usually root is what you want
            menu["console_menu_object"].show_full()

# python3 main.py