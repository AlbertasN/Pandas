import time
import os
import pandas

while True:
    if os.path.exists("temper.csv"):
        data=pandas.read_csv("temper.csv")
        print(data.mean()) #print(data.mean()["st1"])
    else:
        print("File not found.")
    time.sleep(10)