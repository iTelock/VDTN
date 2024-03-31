# 接下来帮我写一个python程序f003moveDirectionDiscre.py，要求：
# 1，使用f002timeSlotDiscre.py运行后返回的数据bus_data
# 2，为bus_data新创建一列，名为moveDirection
# 3，每一个busID对应一辆车，需要计算出车的运动方向，计算方法是根据某条数据的经纬度以及该车下一时刻（参考time）的经纬度计算出运动的方向，方向以正北开始每45度划分为一个方向，一共存在8种方向，对应1,2,3,...,8的数值，计算出方向的数值后存入moveDirection中。如果需要的计算数据不足，则将方向的数值设为0

import pandas as pd
import math

def assign_move_direction(bus_data):
    # 首先，将bus_data转换为DataFrame
    df = pd.DataFrame(bus_data)

    # 对数据进行排序，以确保我们按照时间顺序处理每辆车的数据
    df.sort_values(by=['busID', 'time'], inplace=True)

    # 为数据创建一个新列，用于存储移动方向
    df['moveDirection'] = 0  # 初始值设为0

    # 获取唯一的busID列表
    unique_bus_ids = df['busID'].unique()

    for bus_id in unique_bus_ids:
        # 获取特定busID的所有行
        bus_rows = df[df['busID'] == bus_id]

        # 循环遍历每一行，计算移动方向
        for i in range(len(bus_rows) - 1):
            current_row = bus_rows.iloc[i]
            next_row = bus_rows.iloc[i + 1]

            # 计算经纬度的差值
            delta_lon = next_row['longitude'] - current_row['longitude']
            delta_lat = next_row['latitude'] - current_row['latitude']

            # 计算角度
            angle = math.degrees(math.atan2(delta_lon, delta_lat))
            angle = (angle + 360) % 360  # 角度应该在0到360度之间

            # 计算方向代码
            direction_code = int((angle + 22.5) // 45) + 1
            direction_code = direction_code if direction_code <= 8 else 1

            # 将方向代码存储回数据中
            df.at[current_row.name, 'moveDirection'] = direction_code

    return df.to_dict('records')

# 假设bus_data是前一个程序的输出
# bus_data = ...

# 调用函数，将结果保存回bus_data
# bus_data = assign_move_direction(bus_data)





