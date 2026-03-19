from datetime import date
import matplotlib.pyplot as plt
import meteostat as ms

loc = ms.Point(24.15131333446941, 120.66217283803506)
sv = ms.Point(37.39322970859948, -121.5466194773837)

slist = ms.stations.nearby(sv)
                            #limit最多給3台就好，依據distance距離最近3台
# slist = ms.stations.nearby(sv,limit=3)

# 取出海拔高度 50m 以下的偵測點為依據
below50m = slist[slist['elevation'] < 50]

print("在指定座標附近的偵測點如下: ")
print( below50m )

# (elevation海拔高度)