import pandas as pd

# 定义变量
file_path = '/Users/mr.tao/mycode/VDTN/test/2014-10-01.txt'
save_path = '/Users/mr.tao/mycode/VDTN/dataProcess_get/theMostData.txt'
pathNum = 8
busNum = 12

def select_most_data():
    # 定义列名
    column_names = ["date", "time", "busID", "pathID", "longitude", "latitude", "velocity"]
    
    # 读取数据
    data = pd.read_csv(file_path, names=column_names, sep=',')
    
    # 筛选时间
    data['time'] = pd.to_datetime(data['time'], format='%H:%M:%S').dt.time
    morning_time = pd.to_datetime("7:00:00").time()
    evening_time = pd.to_datetime("19:00:00").time()
    data = data[(data['time'] >= morning_time) & (data['time'] <= evening_time)]
    
    # 找到出现次数最多的pathNum个pathID的数据
    top_path_ids = data.groupby('pathID').size().sort_values(ascending=False).head(pathNum).index
    
    # 初始化一个空的DataFrame用于存储最终的数据
    final_data = pd.DataFrame(columns=column_names)
    
    # 对于每个pathID，找出busNum个出现次数最多的busID的数据
    for path_id in top_path_ids:
        subset = data[data['pathID'] == path_id]
        top_bus_ids = subset.groupby('busID').size().sort_values(ascending=False).head(busNum).index
        subset = subset[subset['busID'].isin(top_bus_ids)]
        final_data = pd.concat([final_data, subset])
    
    # 按照pathID和busID排序
    final_data = final_data.sort_values(by=['pathID', 'busID'])
    
    # 将时间列转换回字符串格式
    final_data['time'] = final_data['time'].apply(lambda x: x.strftime('%H:%M:%S'))
    
    # 保存数据
    final_data.to_csv(save_path, index=False, header=False, sep=',')

if __name__ == '__main__':
    select_most_data()

















# import pandas as pd

# # 定义变量
# file_path = '/Users/mr.tao/mycode/VDTN/test/2014-10-01.txt'
# bus_num = 10
# save_path = '/Users/mr.tao/mycode/VDTN/dataProcess_get/theMostData.txt'

# def select_most_data():
#     # 定义列名
#     column_names = ["date", "time", "busID", "pathID", "longitude", "latitude", "velocity"]
    
#     # 读取数据
#     data = pd.read_csv(file_path, names=column_names, sep=',')
    
#     # 筛选时间
#     data['time'] = pd.to_datetime(data['time'], format='%H:%M:%S').dt.time
#     morning_time = pd.to_datetime("7:00:00").time()
#     evening_time = pd.to_datetime("19:00:00").time()
#     data = data[(data['time'] >= morning_time) & (data['time'] <= evening_time)]
    
#     # 找到数据最多的前bus_num个busID的数据
#     grouped = data.groupby(['busID', 'pathID']).size().reset_index(name='counts')
#     top_bus_ids = grouped.sort_values(by='counts', ascending=False).head(bus_num)['busID']
    
#     # 筛选数据
#     most_data = data[data['busID'].isin(top_bus_ids)]
    
#     # 按busID排序
#     most_data = most_data.sort_values(by='busID')
    
#     # 将时间列转换回字符串格式
#     most_data['time'] = most_data['time'].apply(lambda x: x.strftime('%H:%M:%S'))
    
#     # 保存数据
#     most_data.to_csv(save_path, index=False, header=False, sep=',')

# if __name__ == '__main__':
#     select_most_data()










# import pandas as pd
# from f002saveData import save_data

# # 指定文件路径
# file_path = '/Users/mr.tao/mycode/VDTN/test/2014-10-01.txt'
# # 指定车辆数目
# bus_num = 10
# # 指定保存文件路径和文件名
# save_path = '/Users/mr.tao/mycode/VDTN/dataProcess_get/theMostData.txt'

# # 读取数据集中7:00:00-19:00:00的数据,并选择出现次数多的bus数据
# def read_data(file_path):
#     # 定义列名
#     column_names = ["date", "time", "busID", "pathID", "longitude", "latitude", "velocity"]
    
#     # 从文件中读取数据
#     data = pd.read_csv(file_path, names=column_names, sep=',')

#     # 数据集中的汽车数量（busID）
#     print("数据集中的汽车数量:", data['busID'].nunique())
#     # 数据集中的公交线路数量（pathID）
#     print("数据集中的公交线路数量:", data['pathID'].nunique())

#     # 将时间列转换为 datetime 对象，仅保留时间信息
#     data['time'] = pd.to_datetime(data['time']).dt.time
#     # 定义时间范围
#     start_time = pd.to_datetime('07:00:00').time()
#     end_time = pd.to_datetime('19:00:00').time()
#     # 筛选出指定时间范围内的数据
#     data = data[(data['time'] >= start_time) & (data['time'] <= end_time)]
    
#     # 获取出现最多的前十个公交车ID（改为pathID）
#     top_10_ids = data['pathID'].value_counts().head(bus_num).index.tolist()
#     # 初始化一个空的列表来存储分类的数据
#     grouped_data_list = []
#     # 对每个ID，筛选出该ID对应的所有行，然后将这些行添加到列表中
#     for bus_id in top_10_ids:
#         grouped_data = data[data['pathID'] == bus_id]
#         grouped_data_list.append(grouped_data)
    
#     return grouped_data_list

# # 获取数据最多的公交车数据
# def getTopBus(grouped_data_list, bus_num):
#     # 获取出现次数最多的公交车ID
#     top_num_ids = grouped_data_list['pathID'].value_counts().head(bus_num).index.tolist()
    
#     # 创建过滤条件
#     filter_condition = grouped_data_list['pathID'].isin(top_num_ids)
    
#     # 应用过滤条件，只保留前十个公交车的数据
#     filtered_data = grouped_data_list[filter_condition]
    
#     return filtered_data

# # 调用函数
# filtered_data = read_data(file_path)
# # 打印结果
# # for index, grouped_data in enumerate(filtered_data, 1):
# #     print(f"busID: {grouped_data['busID'].iloc[0]}, 数据条数: {len(grouped_data)}")
# #     print(grouped_data.head())  # 打印每个组的前几行数据，以便查看
# #     print("-" * 50)

# # 保存为txt文件
# save_data(filtered_data,save_path)


