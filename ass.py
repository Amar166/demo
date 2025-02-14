import numpy as np
import pandas as pd

data = pd.read_csv("Data.csv")
data["Timestamp"] = pd.to_datetime(data["Timestamp"], errors="coerce")
data["year"] = data["Timestamp"].dt.year
data_2023 = data[data["year"] == 2023]
data_2023.dropna()
name = data_2023.groupby("city")["PM2.5"].mean().idxmax()
newdata = data_2023[data_2023["city"] == name]
counting = newdata[newdata["PM2.5"]>300]["Timestamp"].count()
percentage = (counting/365.0)*100
print(percentage)
