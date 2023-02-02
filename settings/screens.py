from libqtile import bar, widget
from libqtile.config import Screen

from settings.consts import colors, terminal

def init_screen():
    return Screen(
        top=bar.Bar(
            size=28,
            widgets=[
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    foreground=colors[2],
                    background=colors[0],
                ),
                widget.GroupBox(
                    font="Ubuntu Bold",
                    margin_y=4,
                    margin_x=0,
                    padding_y=5,
                    padding_x=5,
                    borderwidth=1,
                    active=colors[2],
                    inactive=colors[2],
                    rounded=False,
                    highlight_method="block",
                    this_current_screen_border=colors[5],
                    this_screen_border=colors[1],
                    other_current_screen_border=colors[0],
                    other_screen_border=colors[0],
                    foreground=colors[2],
                    background=colors[0],
                ),
                widget.Spacer(
                    length=bar.STRETCH,
                ),
                widget.CheckUpdates(
                    update_interval=2000,
                    distro="Arch",
                    display_format="{updates} Updates",
                    foreground=colors[2],
                    mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(terminal, ' -e sudo pacman -Syu')},
                    background=colors[4]
                ),
                widget.Battery(
                    background=colors[4],
                    foreground=colors[2],
                    low_backround=colors[5],
                    notify_below=15,
                    format="{percent: 2.0%}"
                ),
                # widget.Wlan(
                #     interface="wlp0s20f3",
                #     format="{essid} {percent:2.0%}",
                #     foreground=colors[2],
                #     background=colors[4],
                #     padding=5
                # ),
                widget.Volume(
                    foreground=colors[2],
                    background=colors[5],
                    padding=5
                ),
                widget.Clock(
                    freground=colors[0],
                    background=colors[1],
                    format=" %Y-%m-%d   %H:%M %p",
                ),
                # widget.QuickExit(),
            ],
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        )
    )
