from constants import colors, font_regular, font_bold
from libqtile import bar, widget
from libqtile.config import Screen


def default_screen(external_widgets=()):
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
                    margin_y=5,
                    margin_x=0,
                    padding_y=5,
                    padding_x=5,
                    borderwidth=1,
                    spacing=5,
                    toggle=True,
                    use_mouse_wheel=False,
                    urgent_alert_mode="border",
                    urgent_border=colors["accent"],
                    urgent_text=colors["text"],
                    active=colors["text"],
                    inactive=colors["text"],
                    this_current_screen_border=colors["accent"],
                    this_screen_border=colors["bg"],
                    other_screen_border=colors["bg"],
                    other_current_screen_border=colors["bg"],
                    rounded=False,
                    highlight_method="line",
                    highlight_color=[colors["bg"], colors["bg"]],
                    foreground=colors["bg"],
                    background=colors["bg"],
                ),
                widget.Spacer(
                    length=bar.STRETCH,
                    background=colors["bg"],
                ),
                widget.Clock(
                    background=colors["bg"],
                    foreground=colors["accent"],
                    font=font_regular,
                    format="%a %d  %I:%M %p",
                ),
                widget.Spacer(
                    background=colors["bg"],
                    length=bar.STRETCH,
                ),
                *external_widgets,
                widget.Wlan(
                    font=font_regular,
                    interface="wlp0s20f3",
                    format="{essid}: {percent:2.0%}",
                    foreground=colors["accent"],
                    background=colors["bg"],
                    padding=10,
                ),
                widget.TextBox(
                    text='',
                    foreground=colors["accent"],
                    background=colors["bg"],
                    padding=-7,
                    fontsize=45,
                ),
                widget.TextBox(
                    font=font_regular,
                    text='Vol:',
                    foreground=colors["bg"],
                    background=colors["accent"],
                ),
                widget.Volume(
                    font=font_regular,
                    foreground=colors["bg"],
                    background=colors["accent"],
                ),
                widget.TextBox(
                    text='',
                    background=colors["accent"],
                    foreground=colors["bg"],
                    padding=-7,
                    fontsize=45,
                ),
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
            20,
        ),
    )


secondary_screen_additional_widgets = (
    widget.CPU(
        foreground=colors["accent"],
        background=colors["bg"],
    ),
    widget.TextBox(
        text='',
        background=colors["bg"],
        foreground=colors["accent"],
        padding=-7,
        fontsize=45,
    ),
    widget.Memory(
        foreground=colors["bg"],
        background=colors["accent"],
        measure_mem="G"
    ),
    widget.TextBox(
        text='',
        background=colors["accent"],
        foreground=colors["bg"],
        padding=-7,
        fontsize=45,
    ),
)

main_screen_additional_widgets = (
    widget.Notify(
        background=colors["bg"],
        foreground=colors["accent"],
        audiofile='/usr/share/sounds/gnome/default/alerts/string.ogg'
    ),
    widget.TextBox(
        text='',
        background=colors["bg"],
        foreground=colors["accent"],
        padding=-7,
        fontsize=45,
    ),
    widget.Pomodoro(
        background=colors["accent"],
        foreground=colors["bg"],
        color_active=colors["bg"],
        color_break=colors["bg"],
        color_inactive=colors["bg"]
    ),
    widget.TextBox(
        text='',
        background=colors["accent"],
        foreground=colors["bg"],
        padding=-7,
        fontsize=45,
    ),
)


def init_screens():
    return [default_screen(), default_screen(main_screen_additional_widgets),
            default_screen(secondary_screen_additional_widgets), ]
