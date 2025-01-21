# pyplotstyling
Repo to store layout/styles for plotly and matplotlib

# Usage
## Install package using pip
Clone the repo and install though pip
```bash
git clone https://github.com/konmenel/pyplotstyling.git
cd pyplotstyling
pip install .
```

## Matplotlib
```python
import maplotlib as mpl

mpl.style.use("pyplotstyling.mpl.pps_white_grid")
```

## Plotly
```python
import pyplotstyling.plotly.white_grid
import plotly.io as pio

pio.templates.default = "pps_white_grid"
```
