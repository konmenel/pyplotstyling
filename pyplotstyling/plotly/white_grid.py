"""Loads the custom layout into plotly.io.templates"""
import plotly.io as pio
import plotly.graph_objects as go
from .. import colorscales as _cs


# The customisation is based on plotly white with a few twists
tmp = go.Figure(layout=dict(template=pio.templates["plotly_white"]))
axisdict = dict(
    showline=True,
    linewidth=1,
    linecolor="black",
    mirror=True,
    ticks="inside",
    zerolinecolor="darkgrey",
    zerolinewidth=1,
    gridcolor="darkgrey",
    gridwidth=1,
    minor=dict(
        ticks="inside",
        ticklen=4,
        showgrid=True,
        gridcolor="lightgrey",
        gridwidth=0.75,
    ),
)
tmp.update_layout(
    colorway=_cs.add_opacity_to_colorscale(_cs.discrete_divergent, 0.8),
    font_color="black",
    xaxis=axisdict,
    yaxis=axisdict,
    legend=dict(
        bordercolor="black",
        borderwidth=1,
    ),
)
pio.templates["pps_white_grid"] = pio.to_templated(tmp).layout.template
del tmp, axisdict
