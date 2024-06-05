# About
Auto-clicker made in python.

Uses [Qt5](https://pypi.org/project/PyQt5/) for UI and [Pynput](https://pypi.org/project/pynput/) to emulate the mouse clicks.

# Usage
There are 4 settings total:
## Start-stop keybind
Determines which keyboard key will start and stop the clicker. Default is _E_.

After clicking on the button, _..._ will appear. Then press a key on your keyboard to set that key as the keybind.
## Delay
How long to wait between presses in seconds.
## Max. random delay
After waiting for the fixed amount of seconds specified in _Delay_, wait random amount of time from _0_ to this value.

Set to _0_ to only use fixed delay.
## Button
Specifies, whether to click with _Left_, _Middle_ or _Right_ mouse button.
