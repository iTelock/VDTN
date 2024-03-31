import pandas as pd

def final_process(bus_data, save_path, save_path_before):
    df = pd.DataFrame(bus_data)

    # 创建新列deliveryLevel，假设初始值为0
    # 如果有其他计算deliveryLevel的规则，请根据规则修改此行代码
    df['deliveryLevel'] = 0

    # 调整列的顺序
    columns_order = ['regionCode', 'timeSlot', 'moveDirection', 'contactInterval', 'velocityLevel', 'pathID', 'deliveryLevel', 'time', 'busID', 'longitude', 'latitude', 'velocity']
    df = df.reindex(columns=columns_order)

    # 保存数据到save_path_before指定的路径
    df.to_csv(save_path_before, index=False, header=False, sep=',')
    print(f'Data has been saved to {save_path_before}')

    # 删除指定的列
    df.drop(columns=['time', 'busID', 'longitude', 'latitude', 'velocity'], inplace=True)

    # 保存数据到save_path指定的路径
    df.to_csv(save_path, index=False, header=False, sep=',')
    print(f'Data has been saved to {save_path}')

# 假设bus_data是从前一个程序得到的数据
# bus_data = ...

# 调用函数
# final_process(bus_data)









# import pandas as pd

# def final_process(bus_data, save_path='/Users/mr.tao/mycode/VDTN/deliveryLevel_calculate/x1x6.txt'):
#     df = pd.DataFrame(bus_data)

#     # 创建新列deliveryLevel，假设初始值为0
#     # 如果有其他计算deliveryLevel的规则，请根据规则修改此行代码
#     df['deliveryLevel'] = 0

#     # 删除指定的列
#     df.drop(columns=['time', 'busID', 'longitude', 'latitude', 'velocity'], inplace=True)

#     # 重新排列列的顺序
#     columns_order = ['regionCode', 'timeSlot', 'moveDirection', 'contactInterval', 'velocityLevel', 'pathID', 'deliveryLevel']
#     df = df.reindex(columns=columns_order)

#     # 保存数据到指定的路径
#     df.to_csv(save_path, index=False, header=False, sep=',')

#     print(f'数据已保存入： {save_path}')

# # 假设bus_data是从前一个程序得到的数据
# # bus_data = ...

# # 调用函数
# # final_process(bus_data)






