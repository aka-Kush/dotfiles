from libqtile import bar, qtile
from libqtile.config import DropDown, Group, Key, ScratchPad, Screen
from libqtile.lazy import lazy
from libqtile.widget.battery import Battery, BatteryState
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration, RectDecoration, PowerLineDecoration

from keybindings import keys, mod

groups = []
group_names = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
]
group_labels = ["1", "2", "3", "4", "5", "6", "7"]
# group_labels = ["DEV", "WWW", "MUS", "DIS", "FIL", "CHAT", "VID",]
# group_labels = [" ", " ", " ", " ", " ", " ", " ", " ", "",]
#group_labels = [" "," "," "," "," "," ","",]

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


# Catppuccin bar 1
# screens = [
#     Screen(
#         top=bar.Bar(
#             [   
#                 widget.TextBox(
#                     fontsize=22,
#                     # font="JetBrainsMono Nerd Font Bold",
#                     text="󰣇",
#                     foreground="#ffffff",
#                     # foreground="#000000",
#                     background="#74c7ec",
#                     mouse_callbacks={
#                         "Button1": lambda: qtile.cmd_spawn(
#                         "rofi -show drun" 
#                     )
#                     },
#                     decorations = [
#                         PowerLineDecoration(path="forward_slash")
#                     ]
#                 ),
#                 # widget.Spacer(length=10),
#                 # widget.Sep(foreground="#baRc2de", linewidth=2),
#                 widget.GroupBox(
#                     #active="#a6d189",
#                     fontsize=16,
#                     rounded=False,
#                     this_current_screen_border="#8839ef",
#                     # this_current_screen_border="#000000",
#                     highlight_method="text",
#                     background="#fab387",
#                     borderwidth=0,
#                     hide_unused=True,
#                     decorations = [
#                         PowerLineDecoration(path="forward_slash")
#                     ]
#                 ),
#                 # widget.Sep(foreground="#bac2de", linewidth=2, size_percent=70),
#                 widget.CurrentLayout(
#                     font="JetBrainsMono Nerd Font Mono Bold",
#                     fontsize=16,
#                     foreground="#a6e3a1",
#                 ),
#                 # widget.Sep(foreground="#bac2de", linewidth=2),
#                 widget.WindowName(
#                     foreground="#f9e2af",
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
#                     fontsize=16,
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
#                 widget.Spacer(length=10),
#                 widget.Volume(
#                     # emoji = True,
#                     fontsize=16,
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
#                 widget.Spacer(length=10),
#                 widget.Battery(
#                     # charge_char="",
#                     fontsize=16,
#                     charge_char="",
#                     discharge_char="",
#                     not_charging_char="*",
#                     empty_char="",
#                     full_char="",
#                     format="{char}  {percent:2.0%}",
#                     update_interval=1,
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
#                     length=10
#                 ),
#                 widget.Clock(
#                     fontsize=16,
#                     format="  %I:%M %p - %b %e",
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
#                     length=10
#                 ),
#                 widget.Systray(
#                     fontsize=18,
#                     decorations=[
#                         BorderDecoration(
#                             colour="#fab387",
#                             border_width=[0, 0, 3, 0]
#                         ),
#                     ],
#                 ),
#                 widget.Spacer(
#                     length=10,
#                 ),
#                 widget.TextBox(
#                     fontsize=16,
#                     text="",
#                     foreground="#ffffff",
#                     background="#eb6f92",
#                     mouse_callbacks={
#                         "Button1": lambda: qtile.cmd_spawn(
#                         "bash /home/kush/.config/rofi/scripts/powermenu.sh" 
#                     )
#                     },
#                 ),
#             ],
#             29,
#              background="#1E1E2E",
#              opacity=0.7
#         ),
#     ),
# ]

# Catppuccin bar 2
screens = [
    Screen(
        top=bar.Bar(
            [   
                widget.TextBox(
                    fontsize=22,
                    text="󰣇",
                    foreground="#ffffff",
                    background="#74c7ec",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(
                        "rofi -show drun" 
                    )
                    },
                    decorations = [PowerLineDecoration(path="forward_slash")]
                ),
                widget.CurrentLayout(
                    fontsize=16,
                    foreground="#232634",
                    background="#f9e2af",
                    scale=0.7,
                ),
                widget.Spacer(length=1,decorations=[PowerLineDecoration(path="forward_slash")],background="f9e2af"),
                widget.Spacer(),
                widget.TextBox(
                    fontsize=16,
                    text="",
                    foreground="#ffffff",
                ),
                widget.GroupBox(
                    fontsize=16,
                    rounded=False,
                    # fmt="[{}]",
                    this_current_screen_border="#eb6f92",
                    highlight_method="text",
                    borderwidth=0,
                    hide_unused=True,
                ),
                widget.TextBox(
                    fontsize=16,
                    text="",
                    foreground="#ffffff",
                ),
                widget.Spacer(),
                widget.Spacer(
                    length=5,
                    decorations = [
                        PowerLineDecoration(path="back_slash"),
                    ],
                ),
                widget.Backlight(
                    background = '#f5c2e7',
                    foreground="#232634",
                    backlight_name="amdgpu_bl1",
                    brightness_file="brightness",
                    fontsize=16,
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn("brightnessctl set +5%"),
                        "Button3": lambda: qtile.cmd_spawn("brightnessctl set 5%-"),
                    },
                    format="  {percent:2.0%}",
                    decorations=[PowerLineDecoration(path="back_slash")],
                ),
                widget.Volume(
                    foreground="#232634",
                    background="#f9e2af",
                    fontsize=16,
                    emoji_list=["🔇", "", "", ""],
                    volume_app="pavucontrol",
                    volume_down_command="pactl -- set-sink-volume 0 -5%",
                    volume_up_command="pactl -- set-sink-volume 0 +5%",
                    mute_format="OFF",
                    mute_command="pactl set-sink-mute @DEFAULT_SINK@ toggle",
                    get_volume_command="pamixer --get-volume-human",
                    fmt="  {}",
                    decorations=[PowerLineDecoration(path="back_slash")],
                ),
                widget.Battery(
                    background="#cba6f7",
                    fontsize=16,
                    foreground="#232634",
                    charge_char="",
                    discharge_char="",
                    not_charging_char="*",
                    empty_char="",
                    full_char="",
                    format="{char} {percent:2.0%}",
                    update_interval=1,
                    low_background="#ff0000",
                    low_foreground="#f5f5f5",
                    low_percentage=0.15,
                    notify_below=15,
                    decorations=[PowerLineDecoration(path="back_slash")],
                ),
                widget.Clock(
                    fontsize=16,
                    background="#74c7ec",
                    format="  %I:%M %p - %b %e",
                    update_interval=60.0,
                    foreground="#232634",
                    decorations=[PowerLineDecoration(path="back_slash")],
                ),
                widget.Systray(
                    fontsize=18,
                    foreground="#232634",
                ),
                widget.Spacer(length=5,decorations=[PowerLineDecoration(path="back_slash")]),
                widget.TextBox(
                    fontsize=16,
                    text="",
                    # foreground="#232634",
                    foreground="#ffffff",
                    background="#eb6f92",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(
                        "bash /home/kush/.config/rofi/scripts/powermenu.sh" 
                    )
                    },
                ),
            ],
            29,
             background="#1E1E2E",
             opacity=0.7
        ),
    ),
]


# Nord color bar
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
#                     font="JetBrainsMono Nerd Font Mono Bold",
#                     fontsize=14,
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
#                     foreground="#191724",
#                     fontsize=15,
#                 ),
#                 widget.TextBox(
#                     text='',
#                     background="#f6c177",
#                     foreground="#e0def4",
#                     padding=0,
#                     fontsize=42
#                 ),
#                 widget.Battery(
#                     fontsize=15,
#                     charge_char="",
#                     discharge_char="",
#                     not_charging_char="*",
#                     empty_char="",
#                     full_char="",
#                     format="{char}  {percent:2.0%}",
#                     update_interval=1,
#                     low_foreground="#ff0000",
#                     low_percentage=0.15,
#                     notify_below=15,
#                     foreground="#191724",
#                     background="#e0def4",
#                 ),
#                 widget.TextBox(
#                     text='',
#                     foreground="#eb6f92",
#                     background="#e0def4",
#                     padding=0,
#                     fontsize=42
#                 ),
#                 widget.Volume(
#                     fontsize=15,
#                     emoji_list=["🔇", "", "", ""],
#                     volume_app="pavucontrol",
#                     volume_down_command="pactl -- set-sink-volume 0 -5%",
#                     volume_up_command="pactl -- set-sink-volume 0 +5%",
#                     mute_format="OFF",
#                     mute_command="pactl set-sink-mute @DEFAULT_SINK@ toggle",
#                     get_volume_command="pamixer --get-volume-human",
#                     fmt="  {}",
#                     background="#eb6f92",
#                     foreground="#191724",
#                 ),
#                 widget.TextBox(
#                     text='',
#                     background="#eb6f92",
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
#                     format="%I:%M %p - %b %e",
#                     update_interval=60.0,
#                     fontsize=15,
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
#                     mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("bash /home/kush/.config/rofi/scripts/powermenu.sh")}
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

# gruvbox bar

# class Colors:
#     transparent=  '#00000000'
#     background=   '#1b1b1b'
#     foreground=   '#d4be98'

#     black     = '#282828'
#     red       = '#ea6962'
#     green     = '#a9b665'
#     yellow    = '#d8a657'
#     blue      = '#7daea3'
#     magenta   = '#d3869b'
#     cyan      = '#89b482'
#     white     = '#ddc7a1'
#     gray      = '#32302f'
#     graylight = '#45403d'
    
# palette = Colors()

# class Preferences:
#     terminal            =   "kitty"
#     browser             =   "firefox"
#     private             =   "firefox --private-window"
#     file_manager        =   "thunar"
#     screenshot_tool     =   'gnome-screenshot -i'
#     code_editor         =   "code"
#     launcher            =   "rofi -show drun"
#     # power_menu          =   os.path.expanduser('~/.local/bin/powermenu.sh')
#     font                =   'JetBrainsMono Nerd Font'
#     corner              =   8

# prefs = Preferences()

# widget_list_gruvbox=[  
#     widget.TextBox(
#         text="  󰣇   ",
#         foreground=palette.blue, 
#         font=prefs.font, fontsize=18,
#         mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(prefs.launcher)},
#         margin=7,
#         decorations=[
#             RectDecoration(
#                 filled=True,
#                 colour=palette.graylight,
#                 padding=5,
#                 radius=8
#             ),
#         ],
#     ),
#     widget.GroupBox(  
#         this_current_screen_border=palette.blue, 
#         active=palette.yellow, 
#         inactive=palette.background,
#         highlight_method='text', 
#         borderwidth=0, margin_x=11, padding=0,
#         font=prefs.font, fontsize=18,
#         decorations=[
#             RectDecoration(
#                 filled=True,
#                 colour=palette.graylight,
#                 padding=5,
#                 radius=8
#             ),
#         ],
#     ),
#     widget.WindowName(
#         foreground=palette.green,
#         markup=True,
#         font="JetBrainsMono Nerd Font Mono Bold",
#         fontsize=14,
#         max_chars=63,
#     ),
#     widget.Spacer(),
#     widget.Volume(
#         fontsize=14,
#         padding=12,
#         margin=7,
#         emoji_list=["🔇", "", "", ""],
#         volume_app="pavucontrol",
#         volume_down_command="pactl -- set-sink-volume 0 -5%",
#         volume_up_command="pactl -- set-sink-volume 0 +5%",
#         mute_format="OFF",
#         mute_command="pactl set-sink-mute @DEFAULT_SINK@ toggle",
#         get_volume_command="pamixer --get-volume-human",
#         fmt="  {}",
#         foreground=palette.black,
#         decorations=[
#             RectDecoration(
#                 filled=True,
#                 colour=palette.yellow,
#                 padding=5,
#                 radius=8
#             ),
#         ],
#     ),
#     widget.Battery(
#         charge_char="",
#         fontsize=14,
#         foreground=palette.black,
#         padding=12,
#         margin=7,
#         # charge_char="",
#         discharge_char="",
#         not_charging_char="*",
#         format="{char}  {percent:2.0%}",
#         update_interval=1,
#         low_background=palette.red,
#         low_foreground="#f5f5f5",
#         low_percentage=0.15,
#         notify_below=15,
#         decorations=[
#             RectDecoration(
#                 filled=True,
#                 colour=palette.magenta,
#                 padding=5,
#                 radius=8
#             ),
#         ],
#     ),
#     widget.Clock(  
#         foreground=palette.black, 
#         format="   󱨴 %a, %d %b   ",        
#         font=prefs.font,
#         fontsize=14,
#         padding=12,
#         margin=7,
#         decorations=[
#             RectDecoration(
#                 filled=True,
#                 colour=palette.green,
#                 padding=5,
#                 radius=8
#             ),
#         ],
#     ),
#     widget.Clock(  
#         foreground=palette.black, 
#         format="   󱦟 %I:%M   ",        
#         font=prefs.font, fontsize=14,
#         decorations=[
#             RectDecoration(
#                 filled=True,
#                 colour=palette.blue,
#                 padding=5,
#                 radius=8
#             ),
#         ],
#     ),
#     widget.Systray(),
#     widget.Spacer(
#         length=10
#     ),
# ]


# screens = [
#     Screen(       
#         bottom=bar.Bar(
#             widget_list_gruvbox,
#             size=35, opacity=1,
#             border_width=[0,0,0,0], #N E S W
#             background=palette.background, 
#             # margin=[0,5,5,5],
#         ),
#     ),
# ]
