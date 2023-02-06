from constants import mod
from libqtile.command import lazy
from libqtile.config import Group, Key, Match


def init_groups(keys: list[Key]):
    workspaces = [
        Group("1", label="Term", screen_affinity=1),
        Group("2", label="Net", screen_affinity=1, matches=[Match(wm_class="brave-browser")]),
        Group("3", label="Prog", screen_affinity=1, matches=[Match(wm_class="jetbrains-pycharm")]),
        Group("4", label="Sett", screen_affinity=1, matches=[Match(wm_class="blueman-manager"), Match("pavucontrol")]),
        Group("5", label="Misc", init=False, screen_affinity=1, ),
        Group("6", label="Misc", init=False, screen_affinity=2, ),
        Group("7", label="File", screen_affinity=2, matches=[Match(wm_class="org.gnome.Nautilus")]),
        Group("8", label="Music", screen_affinity=2, matches=[Match(wm_class="spotify")]),
        Group("9", label="Dsc", init=False, screen_affinity=2, matches=[Match(wm_class="discord")]),
        Group("0", label="Teams", screen_affinity=2, matches=[Match(wm_class="microsoft teams - preview")]),
    ]
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
