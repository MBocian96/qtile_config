from constants import colors, font_regular, font_bold
from libqtile import bar, widget
from libqtile.config import Screen

background_break = widget.TextBox(
        text='◥',
        background=colors["bg"],
        foreground=colors["accent"],
        padding=-5,
        fontsize=60,
    )

accent_break = widget.TextBox(
        text='◥',
        background=colors["accent"],
        foreground=colors["bg"],
        padding=-5,
        fontsize=60,
    )



def default_screen(external_widgets=()):
    return Screen(
        wallpaper='~/.config/qtile/plane.jpg',
        wallpaper_mode='stretch',
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
                    toggle=False,
                    use_mouse_wheel=False,
                    urgent_alert_method="border",
                    urgent_border=colors["alert"],
                    urgent_text=colors["text"],
                    active=colors["text"],
                    inactive=colors["text"],
                    this_current_screen_border=colors["accent"],
                    this_screen_border=colors["bg"],
                    other_screen_border=colors["bg"],
                    other_current_screen_border=colors["bg"],
                    rounded=False,
                    highlight_method="block",
                    highlight_color=[colors["accent"], colors["bg"]],
                    oreground=colors["bg"],
                    background=colors["bg"],
					disable_drag=True,
                ),
                widget.Spacer(
                    length=bar.STRETCH,
                    background=colors["bg"],
                ),
                widget.Clock(
                    background=colors["bg"],
                    foreground=colors["accent"],
                    font=font_regular,
                    format="%a %d",
                ),
                widget.Clock(
                    background=colors["bg"],
                    foreground=colors["accent"],
                    font=font_bold,
                    fontsize = 15,
                    format="%I:%M %p",
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
                background_break,
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
                accent_break,
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
    background_break,
    widget.Memory(
        foreground=colors["bg"],
        background=colors["accent"],
        measure_mem="G"
    ),
    accent_break,
)

main_screen_additional_widgets = (
    # widget.Notify(
        # background=colors["bg"],
        # foreground=colors["accent"],
        # audiofile='/usr/share/sounds/gnome/default/alerts/string.ogg'
    # ),
    # background_break,
    # widget.Pomodoro(
    #     background=colors["accent"],
    #     foreground=colors["bg"],
    #     color_active=colors["bg"],
    #     color_break=colors["bg"],
    #     color_inactive=colors["bg"]
    # ),
    # accent_break,
)

def init_screens():
    return [default_screen(), default_screen(main_screen_additional_widgets),
            default_screen(secondary_screen_additional_widgets), ]
