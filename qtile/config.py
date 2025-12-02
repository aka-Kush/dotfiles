# Default imports
import os
import subprocess
from libqtile import hook

# user files imports
from keybindings import *
from bar import *
from layouts import *

# autostart script
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])