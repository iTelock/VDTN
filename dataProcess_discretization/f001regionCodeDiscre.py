import pandas as pd

def process_data(bus_data):
    df = pd.DataFrame(bus_data)
    
    # 删除date列
    df.drop(columns=['date'], inplace=True)
    
    # 计算中心坐标
    center_lat = df['latitude'].mean()
    center_lon = df['longitude'].mean()
    
    # 定义区域边界
    lon_min = center_lon - 35 / 2 / 111  # 35 km宽
    lon_max = center_lon + 35 / 2 / 111
    lat_min = center_lat - 25 / 2 / 111  # 25 km高
    lat_max = center_lat + 25 / 2 / 111
    
    # 计算每个矩形的宽和高
    rect_width = (lon_max - lon_min) / 7
    rect_height = (lat_max - lat_min) / 5
    
    # 初始化regionCode列为0
    df['regionCode'] = 0
    
    # 计算每条数据的区域码
    for index, row in df.iterrows():
        if lon_min <= row['longitude'] <= lon_max and lat_min <= row['latitude'] <= lat_max:
            col = int((row['longitude'] - lon_min) / rect_width)
            row_num = int((row['latitude'] - lat_min) / rect_height)
            region_code = row_num * 7 + col + 1
            df.at[index, 'regionCode'] = region_code
        else:
            df.drop(index, inplace=True)  # 如果数据不在区域内，则删除数据

    # 将更新后的数据转换回字典列表，并返回
    return df.to_dict('records')

# 假设bus_data是从前一个程序得到的数据
# bus_data = ...

# 调用函数，将结果保存回bus_data
# bus_data = process_data(bus_data)
