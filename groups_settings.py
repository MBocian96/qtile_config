from constants import mod
from libqtile.command import lazy
from libqtile.config import Group, Key, Match

#def latest_group(qtile):
#    qtile.current_screen.set_group(qtile.current_screen.previous_group)

#def next_group(qtile):
#    return qtile.current_screen.current_screen

def init_groups(keys: list[Key]):
    workspaces = [
        Group("e", label="Prog", screen_affinity=2, matches=[Match(wm_class="jetbrains-pycharm")]),
        Group("r", label="Net", screen_affinity=2, matches=[Match(wm_class="brave-browser")]),
        Group("t", label="Teams", screen_affinity=2, matches=[Match(wm_class="microsoft teams - preview")]),
        Group("1", label="File", screen_affinity=2, matches=[Match(wm_class="org.gnome.Nautilus")]),
        Group("2", label="Misc", screen_affinity=2),
        Group("3", label="Term", screen_affinity=1),
        Group("4", label="Sett", screen_affinity=1,
              matches=[Match(wm_class="blueman-manager"), Match(wm_class="gnome-control-center"), Match(wm_class="Pavucontrol"),
                       Match(wm_class="pavucontrol")]),
        Group("5", label="Music", screen_affinity=2, matches=[Match(wm_class="spotify")]),
        Group("6", label="Misc", screen_affinity=2),
    ]

#    keys += [Key([mod], "[", lazy.function(latest_group))]
#    keys += [Key([mod], "]", lazy.function(latest_group))]

    for i in workspaces:
        keys.extend(
            [
                # mod1 + letter of group = switch to group
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                ),
                # mod1 + shift + letter of group = switch to & move focused window to group
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                ),
                # Or, use below if you prefer not to switch to that group.
                # # mod1 + shift + letter of group = move focused window to group
                # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                #     desc="move focused window to group {}".format(i.name)),
            ]
        )
    return workspaces

