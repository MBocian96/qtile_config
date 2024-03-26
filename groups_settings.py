from constants import mod
from libqtile.command import lazy
from libqtile.config import Group, Key, Match

#def latest_group(qtile):
#    qtile.current_screen.set_group(qtile.current_screen.previous_group)

#def next_group(qtile):
#    return qtile.current_screen.current_screen

def init_groups(keys: list[Key]):
    workspaces = [
        Group("e", label="e: Prog",   screen_affinity=2, matches=[Match(wm_class="jetbrains-pycharm")]),
        Group("r", label="r: Net",    screen_affinity=2, matches=[Match(wm_class="brave-browser")]),
        Group("t", label="t: Teams",  screen_affinity=2, matches=[Match(wm_class="microsoft teams - preview")]),
        Group("f", label="f: Term",   screen_affinity=1),
        Group("g", label="g: File",   screen_affinity=2, matches=[Match(wm_class="org.gnome.Nautilus")]),
        Group("z", label="z: Zim",    screen_affinity=2, matches=[Match(wm_class="Zim")]),
        Group("x", label="x: Dscrd",  screen_affinity=2, matches=[Match(wm_class="discord")]),
        Group("c", label="c: Slck",   screen_affinity=2, matches=[Match(wm_class="slack")]),
        Group("v", label="v: Music",  screen_affinity=2, matches=[Match(wm_class="spotify")]),
        Group("b", label="b: Sett",   screen_affinity=2,
              matches=[Match(wm_class="blueman-manager"), Match(wm_class="gnome-control-center"), Match(wm_class="Pavucontrol"),
                       Match(wm_class="Solaar"), Match(wm_class="pavucontrol")]),
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

