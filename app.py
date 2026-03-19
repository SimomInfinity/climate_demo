from datetime import date
import matplotlib.pyplot as plt
import meteostat as ms

# Specify location and time range

"""
    ms.Point( lat , long )  緯度 , 經度
"""

POINT2 = ms.Point(50.1155, 8.6842, 113)  # 後面113指示調整參數值
POINT = ms.Point(24.151181173172503, 120.66323499279206)  # 巨匠公益
START = date(2025, 1, 1)
END = date(2025, 12, 31)

# (Get nearby weather stations 先找可用的 偵測點)
stations = ms.stations.nearby(POINT, limit=4) # 給予 stations 座標 並尋找附近的偵測點 抓回前四台 進行資料的擷取

# Get daily data & perform interpolation 時間跟資料填入
ts = ms.daily(stations, START, END) # 從這些機器取出指定時段內的 資料

print("-------------- Time Serie ------------")
print( ts )
print("-------------- Time Serie ------------")

# 資料結構
df = ms.interpolate(ts, POINT).fetch() #(interpolate插值)
df.to_csv("./weather_tc.csv", index=False)
# print(df)
# df --> sql server database 存放 ---> power bi
# df --> power bi 做分析 ( df to_csv  --> import power bi)

# Plot line chart including average, minimum and maximum temperature
df.plot(y=[ms.Parameter.TEMP, ms.Parameter.TMIN, ms.Parameter.TMAX])
plt.show()