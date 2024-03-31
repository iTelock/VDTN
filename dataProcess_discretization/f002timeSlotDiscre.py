


import pandas as pd
from datetime import datetime, timedelta

def assign_time_slot(bus_data):
    # 首先，将bus_data转换为DataFrame
    df = pd.DataFrame(bus_data)
    
    # 定义开始和结束时间
    start_time = datetime.strptime('07:00:00', '%H:%M:%S')
    end_time = datetime.strptime('19:00:00', '%H:%M:%S')
    
    # 定义一个函数来计算时间段
    def calculate_time_slot(row):
        current_time = datetime.strptime(row['time'], '%H:%M:%S')
        
        # 如果时间在指定范围外，可以返回0或者其他特定值，或者处理为异常
        if not (start_time <= current_time <= end_time):
            return 0
        
        # 计算时间差（以分钟为单位）
        time_difference = (current_time - start_time).seconds / 60
        
        # 计算时间段
        time_slot = int(time_difference / 15) + 1
        
        return time_slot
    
    # 为每条数据计算时间段，并存储在新的timeSlot列中
    df['timeSlot'] = df.apply(calculate_time_slot, axis=1)
    
    return df.to_dict('records')

# 假设bus_data是前一个程序的输出
# bus_data = ...

# 调用函数，将结果保存回bus_data
# bus_data = assign_time_slot(bus_data)







