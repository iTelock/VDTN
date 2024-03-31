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













# 历史版本：每个数据都能得到区域码，35个区域覆盖全部面积
# import pandas as pd

# def assign_region_code(bus_data):
#     # 首先，将bus_data转换为DataFrame
#     df = pd.DataFrame(bus_data)
    
#     # 删除date列
#     df.drop(columns=['date'], inplace=True)
    
#     # 计算经纬度的最小和最大值以确定边界
#     min_longitude, max_longitude = df['longitude'].min(), df['longitude'].max()
#     min_latitude, max_latitude = df['latitude'].min(), df['latitude'].max()
    
#     # 计算每个矩形的宽度和高度
#     width = (max_longitude - min_longitude) / 7
#     height = (max_latitude - min_latitude) / 5
    
#     # 定义一个函数来计算区域码
#     def calculate_region_code(row):
#         # 计算经纬度相对于最小经纬度的偏移
#         offset_longitude = row['longitude'] - min_longitude
#         offset_latitude = row['latitude'] - min_latitude
        
#         # 计算该点所在的列和行
#         col = int(offset_longitude / width)
#         row = int(offset_latitude / height)
        
#         # 计算区域码
#         # 注意：由于我们是从左到右、从上到下编号，所以行索引应该是反向的
#         region_code = row * 7 + col + 1
        
#         return region_code
    
#     # 为每条数据计算区域码，并存储在新的regionCode列中
#     df['regionCode'] = df.apply(calculate_region_code, axis=1)
    
#     return df.to_dict('records')

# 假设bus_data是前一个程序的输出
# bus_data = ...

# 调用函数，将结果保存回bus_data
# bus_data = assign_region_code(bus_data)




