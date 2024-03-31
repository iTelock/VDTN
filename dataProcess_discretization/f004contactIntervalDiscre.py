# 接下来帮我写一个python程序f004contactIntervalDiscre.py，要求：
# 1，使用f003moveDirectionDiscre.py运行后返回的数据bus_data
# 2，为bus_data新创建一列，名为contactInterval
# 3，数据中的busID代表不同的车，如果一辆车附近100m范围内有其他车，则称为辆车相遇；现在要计算每辆车和其他车相遇的平均间隔时间，并转化为间隔值，也就是以300秒为粒度，0-300秒视为1,301-600秒视为2……超过3000情况的按照3000秒处理，如果一辆车平均388秒遇到一次其他车辆，则它的间隔值为2。最终将间隔值对应busID存入contactInterval中
# 4，平均间隔时间可以用某车出现的总时间除以遇到车辆的次数（某一时刻遇到多辆车也算为一次）来计算，总时间是指某车出现的最后时刻和初次出现时刻之间的时间

import pandas as pd
import numpy as np

# 设置车辆的信号范围（这里是经纬度，1经纬度约为111千米，这里视为100km）
busDistance = 0.03

def calculate_distance(row1, row2):
    # 简单的欧氏距离计算
    return np.sqrt((row1['longitude'] - row2['longitude']) ** 2 +
                   (row1['latitude'] - row2['latitude']) ** 2)

def assign_contact_interval(bus_data):
    df = pd.DataFrame(bus_data)
    
    # 将时间字符串转换为时间对象以计算时间差
    df['datetime'] = pd.to_datetime(df['time'], format='%H:%M:%S')
    
    # 初始化contactInterval列为0
    df['contactInterval'] = 0
    
    unique_bus_ids = df['busID'].unique()

    for bus_id in unique_bus_ids:
        bus_rows = df[df['busID'] == bus_id]
        first_time = bus_rows['datetime'].min()
        last_time = bus_rows['datetime'].max()
        total_time = (last_time - first_time).seconds
        
        contact_count = 0

        for i, current_row in bus_rows.iterrows():
            other_rows = df[(df['busID'] != bus_id) & (df['time'] == current_row['time'])]
            for j, other_row in other_rows.iterrows():
                if calculate_distance(current_row, other_row) <= busDistance:  # 假设1单位差异等于100米(这里是经纬度，1经纬度约为111千米)
                    contact_count += 1
                    break  # 如果在当前时间已经有车辆接触，就跳出循环

        if contact_count > 0:
            average_interval = total_time / contact_count
            interval_value = min(int(average_interval / 300) + 1, 10)  # 将时间间隔转换为间隔值，最大为10
        else:
            interval_value = 10  # 如果没有车辆接触，将间隔值设为10
        
        df.loc[df['busID'] == bus_id, 'contactInterval'] = interval_value

    return df.drop(columns=['datetime']).to_dict('records')

# 假设bus_data是前一个程序的输出
# bus_data = ...

# 调用函数，将结果保存回bus_data
# bus_data = assign_contact_interval(bus_data)






