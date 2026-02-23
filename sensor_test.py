import random
import datetime

def get_sensor_data():
    data = 9.8 + random.uniform(-0.1, 0.1)
    return round(data, 4)

print(f"--- 传感器监测中 ---")
print(f"时间: {datetime.datetime.now()}")
print(f"数值: {get_sensor_data()} m/s²")
