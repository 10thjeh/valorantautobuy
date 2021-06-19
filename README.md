# Valorant Autobuy
Python script for automating valorant buy

The demo can be found [here](https://youtu.be/tKZmf_kqllo)

# Dependency

[pyautogui](https://pypi.org/project/PyAutoGUI/) and [pynput](https://pypi.org/project/pynput/)

# Starting the script
1. open valorant
2. open main.py (python -m main.py, or other command you use for running py script)
3. press f1 to autobuy
4. press f12 to stop the script

actually step 1 and 2 can be flipped over, just do to your content of your heart

# Using the autobuy

Press F1 to trigger the autobuy, make sure the shop is closed so the script can work properly (this script is, no shit, not integrated to valorant so i cant detect if the shop is opened or not, or maybe you can but im too lazy to implement it)


# Using config.txt

now autobuy uses config.txt to config your autobuy, list of the weapons that recognizeable by the script:
* ability_1
* ability_2
* ability_signature
* small_shield
* big_shield
* shorty
* frenzy
* ghost
* sheriff
* stinger
* spectre
* bucky
* judge
* bulldog
* guardian
* phantom
* vandal
* marshall
* operator
* ares
* odin

edit the config.txt file and add the weapon, each weapon separated by newline (enter key)

for example, default config.txt would look like this:
```
vandal
sheriff
big_shield
ability_1
ability_2
```

if you want to replace vandal with operator, just edit the config.txt file to look like this:
```
operator
sheriff
big_shield
ability_1
ability_2
```

unknown weapon will be ```pass``` 'ed

# Status of the project
Currently it is still beta and looking for more bugs

Tested on 1080p and 720p
