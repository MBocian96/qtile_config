from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

from settings.consts import mod


def init_groups(keys):
    workspaces = [
        Group("1", label="Term", screen_affinity=1, matches=[Match(wm_class=["kgx"])]),
        Group("2", label="Brave", screen_affinity=1, matches=[Match(wm_class=["brave-browser"])]),
        Group("3", label="Charm", screen_affinity=1, matches=[Match(wm_class=["jetbrains-pycharm"])]),
        Group("4", matches=[Match(wm_class=[])]),
        Group("5", matches=[Match(wm_class=[])]),
        Group("6", matches=[Match(wm_class=[])]),
        Group("7", matches=[Match(wm_class=[])]),
        Group("8", matches=[Match(wm_class=[])]),
        Group("9", label="Spotify", screen_affinity=2, matches=[Match(wm_class=["spotify"])]),
        Group("0", label="Teams", screen_affinity=2, matches=[Match(wm_class=["microsoft teams - preview"])]),
    ]
    for group in workspaces:
        keys.extend(
            [
                # mod1 + letter of group = switch to group
                Key(
                    [mod],
                    group.name,
                    lazy.group[group.name].toscreen(),
                    desc="Switch to group {}".format(group.name),
                ),
                # mod1 + shift + letter of group = switch to & move focused window to group
                Key(
                    [mod, "shift"],
                    group.name,
                    lazy.window.togroup(group.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(group.name),
                ),
                # Or, use below if you prefer not to switch to that group.
                # # mod1 + shift + letter of group = move focused window to group
                # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                #     desc="move focused window to group {}".format(i.name)),
                #     Key(
                #         [mod, "alt"],
                #         "l",
                #         lazy.window.toscreen(),
                #         desc="Move group to right monitor"
                #     ),
                #     Key(
                #         [mod, "alt"],
                #         "h",
                #         lazy.window.toscreen(),
                #         desc="Move group to right monitor"
                #     ),
            ]
        )
    return workspaces
