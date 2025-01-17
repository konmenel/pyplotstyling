def hex2rgba(hex: str, opac: float = 1.0) -> str:
    """hex to rgba string (eg rgba(123, 456, 789, 1.0))"""
    hex = hex.lstrip("#")
    return f"rgba({int(hex[0:2], 16)}, {int(hex[2:4], 16)}, {int(hex[4:], 16)}, {opac})"


def add_opacity_to_colorscale(colorscale: list[str], opac: float = 1.0) -> list[str]:
    return [f"{hex2rgba(c, opac)}" for c in colorscale]


discrete_divergent = [
    "#e41a1c",
    "#377eb8",
    "#4daf4a",
    "#984ea3",
    "#ff7f00",
    "#ffff33",
    "#a65628",
    "#f781bf",
    "#999999",
]
discrete_grayscale = ["#252525", "#525252", "#737373", "#969696", "#bdbdbd"]
