"""Simple plotting routine"""

import plotly
from plotly.graph_objs import Scatter, Layout

def singleplot(sensordata, thetitle):
    """ function to make a simple scatter plot
    returns the htmlstring with respective data
    """
    plotstring = plotly.offline.plot({
        "data": [Scatter(x=sensordata[0], y=sensordata[1])],
        "layout": Layout(title=thetitle)
    })

    return plotstring
