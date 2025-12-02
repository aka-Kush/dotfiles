from keybindings import mod
from libqtile import layout
from libqtile.config import Click, Drag, Match
from libqtile.lazy import lazy

catppuccin_theme = {
    "border_width": 4,
    "margin": 6,
    "border_focus": "#eb6f92",
    "border_normal": "#808080",
    "border_on_single": "#eb6f92",
}

gruvbox_theme = {
    "border_width": 5,
    "margin": 6,
    "border_focus": "#d8a657",
    "border_normal": "#ddc7a1",
    "border_on_single": "#d8a657",
}

current_theme = catppuccin_theme


layouts = [
    layout.MonadTall(**current_theme),
    layout.MonadWide(**current_theme),
    layout.Bsp(**current_theme),
    layout.Tile(
        border_focus="#eb6f92", border_normal="#808080", border_on_single="#eb6f92",shift_windows=True
    ),
    layout.Max(),
]


# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod, "shift"], "Button1", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button1", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=current_theme["border_focus"],
    border_normal=current_theme["border_normal"],
    border_width=4,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="copyq"),  # copyq clipboard manager 
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="blueman-manager"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="pavucontrol"),
        Match(wm_class="protonvpn-app"),
        Match(wm_class="Alacritty"),
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
# wl_xcursor_size = 24

# wl_input_rules = {
#     "type:touchpad": InputConfig(tap=True, natural_scroll=True, dwt=True),
# }


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
