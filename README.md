<div class="markdown prose w-full break-words dark:prose-invert dark"><h1>Termtek Python Module</h1><h2>Console Menu System</h2><p>The <code>Termtek Python Module</code> is a library that provides a console menu system for Python programs. It is designed to be easy to use for inexperienced programmers while also providing a reliable foundation for experienced developers.</p><h2>Features</h2><ul><li>A back button that automatically returns to the previous menu</li><li>A verbose debugger that can be turned on for debugging purposes</li><li>The ability to execute functions or navigate to other menus from menu options</li></ul><h2>Usage</h2><p>To use the library, you need to define your menus as dictionaries containing a <code>menu_name</code>, a <code>banner</code> displayed at the top of the menu, and a list of <code>menu_options</code>. Each menu option is a list containing a <code>key</code>, a <code>label</code> describing the action, and a <code>func</code> that can be a function to execute or a dictionary with a <code>goto</code> key that references another menu.</p><p>Once you have defined your menus, you can use the <code>ttk.build_console_menu_objects</code> function to create a <code>console_menu_object</code> attribute for each menu. You can then use the <code>show_full</code> method of the <code>console_menu_object</code> to display the menu and handle user input.</p><p>The library also provides a <code>build_fancy_font</code> function that can be used to create a banner with a custom font.</p><p>Overall, the <code>Termtek Python Module</code> provides a simple and customizable solution for creating console menus in Python programs.</p></div>

```
fullbl00m@bl00mb0x:~/Desktop/golden-ai$ python3 main.py 

█▀▄▀█ ▄▀█ █ █▄░█    █▀▄▀█ █▀▀ █▄░█ █░█
█░▀░█ █▀█ █ █░▀█    █░▀░█ ██▄ █░▀█ █▄█

[ test1 ]: Test function one
[ test2 ]: Test funtion two
[ openai ]: Play with Openai API
[ settings ]: Change settings for the program
[ exit ]: Exit the program

Please select an option: exit

```

This is a simple diagram of the test menu structure that is currently in main.py

```
root_menu
|
|--- test1 (Test function one)
|--- test2 (Test function two)
|
|--- openai (Play with Openai API)
|     |--- test1 (Test openai function one)
|     |--- test2 (Test openai function two)
|     |--- aisettings (Change settings for openai)
|     |     |--- test1 (Test openai settings function one)
|     |     |--- test2 (Test openai settings function two)
|     |     |--- Go Back (Return to previous menu)
|     |
|     |--- Go Back (Return to previous menu)
|
|
|--- settings (Change settings for the program)
|     |--- password (Change your account password)
|     |--- email (Change your account email)
|     |--- Go Back (Return to previous menu)
|
|--- exit (Exit the program)

```


The inspiration for this project was to simplify and accelerate the creation and maintenance of interconnected console menu programs.

<b>Quality of life features:</b><br>
The back buttons will automatically map to the menu that called it so you don't have to worry about that.<br>
There is a verbose debugger that I built for myself but you can use it if you want to modify the module.
If you want just set Debug to True in modules/consolemodule.py or override it in main.py

The secret to its magic revolves around the fact that the menu_options you supply it can point to...

<ul>
    <li><b>Any Function Reference</b></li>
    <li><b>Any Menu Name</b></li>
</ul>

The menu_option is a List that is comprised of: [ <b>key</b>, <b>label</b>, <b>func</b> ]
<ul>
    <li><b>key:</b> This is the keyword that the user will type to activate a menu_option in your program</li>
    <li><b>label:</b> This is the text that will describe the action of your menu option</li>
    <li><b>func:</b> This is the most important part of the project. This points to either a function to run or the name of another menu_name that you want to reference.</li>
</ul>

Below is an example of a menu dictionary that you will customize in the main.py file.

```
root_menu = {
    "menu_name": "root_menu",                                                           # REQUIRED STRING
    "banner": ttk.build_fancy_font("Main Menu"),                                        # REQUIRED STRING
    "menu_options": [                                                                   # REQUIRED LIST
        ["test1", "Test function one", testone],
        ["test2", "Test funtion two", testtwo],
        ["openai", "Play with Openai API", {"goto": "openai_api_menu"}],
        ["settings", "Change settings for the program", {"goto": "settings_menu"}],
        ["exit", "Exit the program", exit]
    ]
}
```
As you can see in the example above the "menu_options" can point to either a python function as the 3rd argument, or you can use a goto that just points to another menu_name of your choosing and it will automatically handle the rest.

Another interesting thing to note is that I am using the ttk.build_fancy_font() function of the termtek module to return an ascii font of the string. Feel free to use it. I made it for you :p

# How to run
```
git clone git@github.com:FULLBL00M/termtek-python-console-menu-system.git
cd termtek-python-console-menu-system/
python3 main.py
```

# How to edit
You should be able to figure out whats going on in the main.py file if you read these docs.
But the required steps are...

1) Create your menu blocks in main.py
2) Ensure they match the template structure
3) add all menu block vars to a list in the way you prefer
4) submit the List to the ttk.build_console_menu_objects(all_menus) function
5) set your default menu in the __main__ function

If you are looking at this for somereason and want to know more hit me up on discord.

<br>
Created by @fullbl00m#1224 on discord
           <br>@FULLBL00M on github


