from libqtile import bar, qtile
from libqtile.config import DropDown, Group, Key, ScratchPad, Screen
from libqtile.lazy import lazy
from libqtile.widget.battery import Battery, BatteryState
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration

from keybindings import keys, mod

groups = []
# group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]
group_names = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
]
# group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]
# group_labels = ["DEV", "WWW", "MUS", "DIS", "FIL", "CHAT", "VID",]
# group_labels = [" ", " ", " ", " ", " ", " ", " ", " ", "",]
group_labels = [
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    "",
]

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
        )
    )

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

# scratchpads
groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown("term", "kitty", height=0.8, width=0.6, x=0.2, y=0.1),
            DropDown("file", "thunar", height=0.8, width=0.6, x=0.2, y=0.1),
        ],
    )
)

keys.extend(
    [
        Key(["control"], "1", lazy.group["scratchpad"].dropdown_toggle("term")),
        Key(["control"], "2", lazy.group["scratchpad"].dropdown_toggle("file")),
    ]
)


# bar

widget_defaults = dict(
    # font="UbuntuMono Nerd Font",
    font="JetBrainsMono Nerd Font",
    fontsize=14,
    padding=10,
)
extension_defaults = widget_defaults.copy()


# screens = [
#     Screen(
#         top=bar.Bar(
#             [
#                 widget.Sep(
#                     linewidth=0,
#                     padding=6
#                 ),
#                 widget.GroupBox(
#                     active="#ffffff",
#                     rounded=False,
#                     highlight_color="#c4a7e7",
#                     highlight_method="line",
#                     borderwidth=0,
#                     inactive="#808080"
#                 ),
#                 widget.WindowName(
#                     foreground="#eb6f92",
#                     markup=True,
#                     font="CodeNewRoman Nerd Font",
#                     fontsize=15,
#                     max_chars=63
#                 ),
#                 widget.TextBox(
#                     text='',
#                     background="#282a36",
#                     foreground="#f6c177",
#                     padding=0,
#                     fontsize=42
#                 ),
#                 widget.TextBox(
#                     text=' ',
#                     background="#f6c177",
#                     foreground="#191724",
#                     padding=7
#                 ),
#                 widget.CurrentLayout(
#                     background="#f6c177",
#                     foreground="#191724"
#                 ),
#                 widget.TextBox(
#                     text='',
#                     background="#f6c177",
#                     foreground="#e0def4",
#                     padding=0,
#                     fontsize=42
#                 ),
#                 widget.CPU(
#                     background="#e0def4",
#                     foreground="191724",
#                     format="󰘚 {load_percent}%"
#                 ),
#                 widget.TextBox(
#                     text='',
#                     foreground="#eb6f92",
#                     background="#e0def4",
#                     padding=0,
#                     fontsize=42
#                 ),
#                 widget.Memory(
#                     format="{MemUsed: .0f}{mm}",
#                     background="#eb6f92",
#                     foreground="#191724",
#                     interval=1.0
#                 ),
#                 widget.TextBox(
#                     text='',
#                     background="#eb6f92",
#                     foreground="#9ccfd8",
#                     padding=0,
#                     fontsize=42
#                 ),
#                 widget.Net(
#                     interface="wlan0",
#                     format=" {interface}: {down} ↓↑ {up}",
#                     background="#9ccfd8",
#                     foreground="#191724",
#                     update_interval=1.0
#                 ),
#                 widget.TextBox(
#                     text='',
#                     background="#9ccfd8",
#                     foreground="#c4a7e7",
#                     padding=0,
#                     fontsize=42
#                 ),
#                 widget.TextBox(
#                     text='',
#                     background="#c4a7e7",
#                     foreground="#191724",
#                     padding=7
#                 ),
#                 widget.Clock(
#                     background="#c4a7e7",
#                     foreground="#191724",
#                     # format="%H:%M - %d/%m/%Y",
#                     format="%I:%M %p - %b %e",
#                     update_interval=60.0
#                 ),
#                 widget.TextBox(
#                     text='',
#                     background="#c4a7e7",
#                     foreground="#282a36",
#                     padding=0,
#                     fontsize=42
#                 ),
#                 widget.Systray(
#                     foreground="#ffffff"
#                 ),
#                 # widget.Battery(),
#                 widget.Spacer(
#                     length=12,
#                     background="#282a36"
#                 ),
#                 widget.TextBox(
#                     text='',
#                     background="#282a36",
#                     foreground="#CAFFBF",
#                     padding=0,
#                     fontsize=42
#                 ),
#                 widget.TextBox(
#                     text="",
#                     background="#CAFFBF",
#                     foreground="#000000",
#                     mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("python /usr/share/archlinux-logout/archlinux-logout.py")}
#                 ),
#                 widget.Spacer(
#                     length=12,
#                     background="#CAFFBF"
#                 ),
#             ],
#             25,
#             background="#282a36",
#         ),
#     ),
# ]


# screens = [
#     Screen(
#         top=bar.Bar(
#             [
#                 widget.GroupBox(
#                     active="#ffffff",
#                     rounded=False,
#                     highlight_color="#eb6f92",
#                     highlight_method="line",
#                     borderwidth=0,
#                     inactive="#808080",
#                 ),
#                 widget.Sep(foreground="#bac2de", linewidth=2),
#                 # CurrentLayoutIcon(
#                 #     font = "UbuntuMono Nerd Font",
#                 #     fontsize = 1,
#                 #     foreground = "#f9e2af",
#                 #     use_mask = True
#                 # ),
#                 widget.CurrentLayout(
#                     font="JetBrainsMono Nerd Font Mono Bold",
#                     foreground="#a6e3a1",
#                 ),
#                 widget.Sep(foreground="#bac2de", linewidth=2),
#                 widget.WindowName(
#                     foreground="#eb6f92",
#                     markup=True,
#                     font="CodeNewRoman Nerd Font Bold",
#                     fontsize=15,
#                     max_chars=63,
#                 ),
#                 widget.Backlight(
#                     # background = '#b4befe',
#                     # foreground = '#000000',
#                     backlight_name="amdgpu_bl1",
#                     brightness_file="brightness",
#                     fontsize=15,
#                     mouse_callbacks={
#                         "Button1": lambda: qtile.cmd_spawn("brightnessctl set +5%"),
#                         "Button3": lambda: qtile.cmd_spawn("brightnessctl set 5%-"),
#                     },
#                     format="  {percent:2.0%}",
#                     decorations=[
#                         BorderDecoration(
#                             colour="#f5c2e7",
#                             border_width=[0, 0, 3, 0],
#                             padding=0,
#                         ),
#                     ],
#                 ),
#                 widget.Spacer(length=10, background="#1e1e2e"),
#                 widget.Volume(
#                     # emoji = True,
#                     emoji_list=["🔇", "", "", ""],
#                     volume_app="pavucontrol",
#                     volume_down_command="pactl -- set-sink-volume 0 -5%",
#                     volume_up_command="pactl -- set-sink-volume 0 +5%",
#                     mute_format="OFF",
#                     mute_command="pactl set-sink-mute @DEFAULT_SINK@ toggle",
#                     get_volume_command="pamixer --get-volume-human",
#                     fmt="  {}",
#                     decorations=[
#                         BorderDecoration(
#                             colour="#f9e2af",
#                             border_width=[0, 0, 3, 0],
#                             padding=0,
#                         ),
#                     ],
#                 ),
#                 widget.Spacer(length=10, background="#1e1e2e"),
#                 widget.Battery(
#                     # charge_char="",
#                     charge_char="",
#                     discharge_char="",
#                     not_charging_char="*",
#                     empty_char="",
#                     full_char="",
#                     format="{char}  {percent:2.0%}",
#                     update_interval=1,
#                     fontsize=14,
#                     low_background="#ff0000",
#                     low_foreground="#f5f5f5",
#                     low_percentage=0.15,
#                     notify_below=15,
#                     decorations=[
#                         BorderDecoration(
#                             colour="#cba6f7",
#                             border_width=[0, 0, 3, 0],
#                             padding=0,
#                         ),
#                     ],
#                 ),
#                 widget.Spacer(
#                     length=10,
#                     background="#1e1e2e",
#                 ),
#                 widget.Clock(
#                     format="   %I:%M %p - %b %e",
#                     update_interval=60.0,
#                     decorations=[
#                         BorderDecoration(
#                             colour="#74c7ec",
#                             border_width=[0, 0, 3, 0],
#                             padding=0,
#                         ),
#                     ],
#                 ),
#                 widget.Spacer(
#                     length=10,
#                     background="#1e1e2e",
#                 ),
#                 widget.Systray(
#                     decorations=[
#                         BorderDecoration(
#                             colour="#fab387",
#                             border_width=[0, 0, 3, 0],
#                             padding_x=0,
#                         ),
#                     ],
#                 ),
#                 widget.Spacer(
#                     length=10,
#                     background="#1e1e2e",
#                 ),
#                 widget.TextBox(
#                     text="",
#                     foreground="#f38ba8",
#                     mouse_callbacks={
#                         "Button1": lambda: qtile.cmd_spawn(
#                             "python /usr/share/archlinux-logout/archlinux-logout.py"
#                         )
#                     },
#                 ),
#                 widget.Spacer(
#                     length=4,
#                 ),
#             ],
#             25,
#             background="#1e1e2e",
#         ),
#     ),
# ]

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active="#a6d189",
                    fontsize=16,
                    rounded=False,
                    highlight_color="#dd7878",
                    highlight_method="line",
                    borderwidth=0,
                    # inactive="#808080",
                    inactive="#ffffff",
                ),
                widget.Sep(foreground="#bac2de", linewidth=2),
                widget.CurrentLayout(
                    font="JetBrainsMono Nerd Font Mono Bold",
                    fontsize=16,
                    foreground="#a6e3a1",
                ),
                widget.Sep(foreground="#bac2de", linewidth=2),
                widget.WindowName(
                    foreground="#f9e2af",
                    markup=True,
                    font="CodeNewRoman Nerd Font Bold",
                    fontsize=17,
                    max_chars=63,
                ),
                widget.Backlight(
                    # background = '#b4befe',
                    # foreground = '#000000',
                    backlight_name="amdgpu_bl1",
                    brightness_file="brightness",
                    fontsize=16,
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn("brightnessctl set +5%"),
                        "Button3": lambda: qtile.cmd_spawn("brightnessctl set 5%-"),
                    },
                    format="  {percent:2.0%}",
                    decorations=[
                        BorderDecoration(
                            colour="#f5c2e7",
                            border_width=[0, 0, 3, 0],
                            padding=0,
                        ),
                    ],
                ),
                widget.Spacer(length=10),
                widget.Volume(
                    # emoji = True,
                    fontsize=16,
                    emoji_list=["🔇", "", "", ""],
                    volume_app="pavucontrol",
                    volume_down_command="pactl -- set-sink-volume 0 -5%",
                    volume_up_command="pactl -- set-sink-volume 0 +5%",
                    mute_format="OFF",
                    mute_command="pactl set-sink-mute @DEFAULT_SINK@ toggle",
                    get_volume_command="pamixer --get-volume-human",
                    fmt="  {}",
                    decorations=[
                        BorderDecoration(
                            colour="#f9e2af",
                            border_width=[0, 0, 3, 0],
                            padding=0,
                        ),
                    ],
                ),
                widget.Spacer(length=10),
                widget.Battery(
                    # charge_char="",
                    fontsize=16,
                    charge_char="",
                    discharge_char="",
                    not_charging_char="*",
                    empty_char="",
                    full_char="",
                    format="{char}  {percent:2.0%}",
                    update_interval=1,
                    low_background="#ff0000",
                    low_foreground="#f5f5f5",
                    low_percentage=0.15,
                    notify_below=15,
                    decorations=[
                        BorderDecoration(
                            colour="#cba6f7",
                            border_width=[0, 0, 3, 0],
                            padding=0,
                        ),
                    ],
                ),
                widget.Spacer(
                    length=10
                ),
                widget.Clock(
                    fontsize=16,
                    format="  %I:%M %p - %b %e",
                    update_interval=60.0,
                    decorations=[
                        BorderDecoration(
                            colour="#74c7ec",
                            border_width=[0, 0, 3, 0],
                            padding=0,
                        ),
                    ],
                ),
                widget.Spacer(
                    length=10
                ),
                widget.Systray(
                    fontsize=17,
                    decorations=[
                        BorderDecoration(
                            colour="#fab387",
                            border_width=[0, 0, 3, 0]
                        ),
                    ],
                ),
                widget.Spacer(
                    length=10
                ),
                widget.TextBox(
                    fontsize=16,
                    text="",
                    foreground="#ffffff",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(
                            "python /usr/share/archlinux-logout/archlinux-logout.py"
                        )
                    },
                ),
                widget.Spacer(
                    length=6,
                ),
            ],
            29,
            background="#00000000",
        ),
    ),
]
