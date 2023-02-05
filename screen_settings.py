from constants import colors, font_regular, font_bold
from libqtile import bar, widget
from libqtile.config import Screen


def init_screen():
    return Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    padding=10,
                    foreground=colors["accent"],
                    background=colors["bg"],
                ),
                widget.GroupBox(
                    font=font_bold,
                    margin_y=4,
                    margin_x=0,
                    padding_y=5,
                    padding_x=5,
                    borderwidth=1,
                    spacing=5,
                    toggle=True,
                    use_mouse_wheel=False,
                    urgent_alert_mode="border",
                    urgent_border=colors["accent"],
                    urgent_text=colors["accent"],
                    active=colors["text"],
                    inactive=colors["text"],
                    this_current_screen_border=colors["accent"],
                    this_screen_border=colors["bg"],
                    other_screen_border=colors["bg"],
                    other_current_screen_border=colors["bg"],
                    rounded=False,
                    highlight_method="line",
                    foreground=colors["bg"],
                    background=colors["bg"],
                ),
                widget.Spacer(
                    length=bar.STRETCH,
                ),
                widget.Clock(
                    background=colors["bg"],
                    foreground=colors["accent"],
                    font=font_regular,
                    format="%a %d  %I:%M %p",
                ),
                widget.Spacer(
                    length=bar.STRETCH,
                ),
                widget.Wlan(
                    font=font_regular,
                    interface="wlp0s20f3",
                    format="{essid}: {percent:2.0%}",
                    foreground=colors["accent"],
                    background=colors["bg"],
                    padding=5,
                ),
                widget.TextBox(
                    font=font_regular,
                    text='Vol:',
                    foreground=colors["bg"],
                    background=colors["accent"],
                    padding=5,
                ),
                widget.Volume(
                    font=font_regular,
                    foreground=colors["bg"],
                    background=colors["accent"],
                    padding=5
                ),
                # widget.TextBox(
                #     text='',
                #     foreground=colors["accent"],
                #     background=colors["bg"],
                #     padding=0,
                #     fontsize=40,
                # ),
                widget.TextBox(
                    text='Battery: ',
                    font=font_regular,
                    foreground=colors["accent"],
                    background=colors["bg"],
                ),
                widget.Battery(
                    font=font_regular,
                    background=colors["bg"],
                    foreground=colors["accent"],
                    low_foreground=colors["text"],
                    notify_below=15,
                    format="{percent: 2.0%}"
                ),
            ],
            24,
        ),
    )


def init_screens():
    return [init_screen(), init_screen(), init_screen(), ]
