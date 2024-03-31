# 接下来帮我写一个python程序f005velocityDiscre.py，要求如下：
# 1，使用f004contactIntervalDiscre.py运行后返回的数据bus_data
# 2，为bus_data新创建一列，名为velocityLevel
# 3，根据数据中的velocity，计算出其对应的速度等级并存入其velocityLevel，计算规则是[0,24)视为1,[24,48)视为2,以此类推，velocity大于120时视为120处理。

import pandas as pd

def process_velocity(bus_data):
    df = pd.DataFrame(bus_data)

    # 将速度限制在120以内
    df['velocity'] = df['velocity'].apply(lambda x: min(x, 120))
    
    # 计算速度等级，并存入新的列velocityLevel
    df['velocityLevel'] = (df['velocity'] // 24 + 1).astype(int)

    # 将更新后的数据转换回字典列表，并返回
    return df.to_dict('records')

# 假设bus_data是从前一个程序得到的数据
# bus_data = ...

# 调用函数，将结果保存回bus_data
# bus_data = process_velocity(bus_data)






