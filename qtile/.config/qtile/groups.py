from keybindings import keys, mod
from libqtile.config import Group, Key
from libqtile.lazy import lazy

groups= []
# group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]
group_names = ["1", "2", "3", "4", "5", "6", "7",]
# group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]
group_labels = ["DEV", "WWW", "MUS", "DIS", "FIL", "CHAT", "VID",]
# group_labels = [" ", " ", " ", " ", " ", " ", " ", " ", "",]
#group_labels = [" ", " ", " ", " ", " ", " ", "",]

# groups = [Group(i) for i in [
#     "   ", "   ", "   ", "   ", "   ", "   ", "   ",
# ]]

# group_layouts = ["monadtall", "monadtall", "tile", "tile", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            # layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Move focused window to group {}".format(i.name),
            ),
        ]
    )