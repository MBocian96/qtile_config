from constants import colors
from libqtile import layout
from libqtile.config import Match


def init_floating():
    return layout.Floating(
        float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client.
            *layout.Floating.default_float_rules,
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry
        ]
    )

layout_config = {
    "border_focus_stack":[colors['accent'], colors['accent']],
    "border_focus": colors["accent"],
    "border_width": 2,
    "margin": 8
}

def init_layout():
    return [
        # layout.Columns(**layout_config),
        layout.MonadTall(**layout_config ),
        layout.Max(**layout_config),
        # Try more layouts by unleashing below layouts.
         # layout.Stack(num_stacks=2),
         # layout.Bsp(**layout_config ),
         layout.Matrix(**layout_config ),
         # layout.MonadWide(),
         # layout.RatioTile(),
         # layout.Tile(),
         # layout.TreeTab(),
         # layout.VerticalTile(),
         # layout.Zoomy(),

    ]
