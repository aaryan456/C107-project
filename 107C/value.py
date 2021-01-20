import pandas as ps
import csv
import plotly.express as pex

studentdf = ps.read_csv("value.csv")
stdf = studentdf.groupby(["ID", "level"], as_index = False)["attempt"].mean()
fig = pex.scatter(data_frame=stdf, x="ID", y="level", size="attempt", color="attempt")
fig.show()