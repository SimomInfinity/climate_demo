from datetime import date
import matplotlib.pyplot as plt
import meteostat as ms

POINT = ms.Point(24.151181173172503, 120.66323499279206)
START = date(2025, 1, 1)
END = date(2025, 12, 31)

stations = ms.stations.nearby(POINT, limit=4)

ts = ms.daily(stations, START, END)
df = ms.interpolate(ts, POINT).fetch()
df_reset = df.reset_index()
print(df_reset)