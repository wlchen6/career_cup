import random
import datetime

class KalmanFilter:
    def __init__(self, process_variance, measurement_variance, estimated_error, initial_value):
        self.process_variance = process_variance
        self.measurement_variance = measurement_variance
        self.estimated_error = estimated_error
        self.value = initial_value

    def update(self, measurement):
        prediction_error = self.estimated_error + self.process_variance
        kalman_gain = prediction_error / (prediction_error + self.measurement_variance)
        self.value = self.value + kalman_gain * (measurement - self.value)
        self.estimated_error = (1 - kalman_gain) * prediction_error
        return self.value

# Vibe: 模拟真实环境中的重力传感器（带噪声）
kf = KalmanFilter(process_variance=1e-5, measurement_variance=0.1**2, estimated_error=1.0, initial_value=9.8)

print(f"--- 传感器 Vibe Coding 实验 (执行时间: {datetime.datetime.now()}) ---")
print(f"{'步数':<5} | {'原始读数 (带噪声)':<15} | {'滤波后读数 (纯净)':<15}")
print("-" * 50)

for i in range(1, 11):
    raw_data = 9.8 + random.uniform(-0.5, 0.5) # 模拟很大的噪声
    filtered_data = kf.update(raw_data)
    print(f"{i:<5} | {raw_data:<18.4f} | {filtered_data:<18.4f}")

print("-" * 50)
print("Vibe Check: 你看，滤波后的数据是不是非常接近 9.8，且波动极小？这就是算法的力量。")
