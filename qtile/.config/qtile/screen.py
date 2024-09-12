from libqtile import bar, qtile, widget
from libqtile.config import Screen


widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=14,
    padding=10,
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    padding=6
                ),
                # widget.Image(
                #     filename="~/.config/qtile/Archlinux-icon.svg",
                #     scale="False"
                # ),
                # widget.Sep(
                #     linewidth=0,
                #     padding=6
                # ),
                widget.GroupBox(
                    active="#ffffff",
                    rounded=False,
                    highlight_color="#c4a7e7",
                    highlight_method="line",
                    borderwidth=0,
                    inactive="#808080"
                ),
                widget.WindowName(
                    foreground="#eb6f92",
                    markup=True,
                    font="CodeNewRoman Nerd Font",
                    fontsize=15,
                    max_chars=63
                ),
                widget.TextBox(
                    text='',
                    background="#282a36",
                    foreground="#f6c177",
                    padding=0,
                    fontsize=42
                ),
                widget.TextBox(
                    text=' ',
                    background="#f6c177",
                    foreground="#191724",
                    padding=7
                ),
                widget.CurrentLayout(
                    background="#f6c177",
                    foreground="#191724"
                ),
                widget.TextBox(
                    text='',
                    background="#f6c177",
                    foreground="#e0def4",
                    padding=0,
                    fontsize=42
                ),
                widget.CPU(
                    background="#e0def4",
                    foreground="191724",
                    format="󰘚 {load_percent}%"
                ),
                widget.TextBox(
                    text='',
                    foreground="#eb6f92",
                    background="#e0def4",
                    padding=0,
                    fontsize=42
                ),
                widget.Memory(
                    format="{MemUsed: .0f}{mm}",
                    background="#eb6f92",
                    foreground="#191724",
                    interval=1.0
                ),
                widget.TextBox(
                    text='',
                    background="#eb6f92",
                    foreground="#9ccfd8",
                    padding=0,
                    fontsize=42
                ),
                widget.Net(
                    interface="wlan0",
                    format=" {interface}: {down} ↓↑ {up}",
                    background="#9ccfd8",
                    foreground="#191724",
                    update_interval=1.0
                ),
                widget.TextBox(
                    text='',
                    background="#9ccfd8",
                    foreground="#c4a7e7",
                    padding=0,
                    fontsize=42
                ),
                widget.TextBox(
                    text='',
                    background="#c4a7e7",
                    foreground="#191724",
                    padding=7
                ),
                widget.Clock(
                    background="#c4a7e7",
                    foreground="#191724",
                    # format="%H:%M - %d/%m/%Y",
                    format="%I:%M %p - %b %e",
                    update_interval=60.0
                ),
                widget.TextBox(
                    text='',
                    background="#c4a7e7",
                    foreground="#282a36",
                    padding=0,
                    fontsize=42
                ),
                widget.Systray(
                    foreground="#ffffff"
                ),
                # widget.Battery(),
                widget.Spacer(
                    length=12,
                    background="#282a36"
                ),
                widget.TextBox(
                    text='',
                    background="#282a36",
                    foreground="#CAFFBF",
                    padding=0,
                    fontsize=42
                ),
                widget.TextBox(
                    text="",
                    background="#CAFFBF",
                    foreground="#000000",
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("python /usr/share/archlinux-logout/archlinux-logout.py")}
                ),
                widget.Spacer(
                    length=12,
                    background="#CAFFBF"
                ),
            ],
            25,
            background="#282a36",
        ),
    ),
    # Screen(
    #     top=bar.Bar(
    #         [
    #             widget.GroupBox(
    #                 active="#ffffff",
    #                 rounded=False,
    #                 highlight_color="#c4a7e7",
    #                 highlight_method="line",
    #                 borderwidth=0
    #             ),
    #             widget.WindowName(
    #                 foreground="#eb6f92",
    #                 markup=True,
    #                 font="CodeNewRoman Nerd Font",
    #                 fontsize=15,
    #             ),
    #             widget.TextBox(
    #                 text='',
    #                 foreground="#e0def4",
    #                 padding=0,
    #                 fontsize=42
    #             ),
    #             widget.TextBox(
    #                 text=' ',
    #                 background="#e0def4",
    #                 foreground="#191724",
    #                 padding=2
    #             ),
    #             widget.CheckUpdates(
    #                 update_interval=18000,
    #                 display_format="{updates}",
    #                 colour_have_updates="#191724",
    #                 background="#e0def8"
    #             ),
    #             widget.TextBox(
    #                 text='',
    #                 background="#e0def8",
    #                 foreground="#c4a7e7",
    #                 padding=0,
    #                 fontsize=42
    #             ),
    #             widget.TextBox(
    #                 text='',
    #                 background="#c4a7e7",
    #                 foreground="#191724",
    #                 padding=7
    #             ),
    #             widget.Clock(
    #                 background="#c4a7e7",
    #                 foreground="#191724",
    #                 format="%H:%M",
    #                 update_interval=60.0
    #             ),
    #         ],
    #         25,
    #         background="#232136",
    #     ),
    # ),

]
