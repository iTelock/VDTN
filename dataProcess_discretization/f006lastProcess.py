# 接下来帮我写一个python程序f006lastProcess.py，要求如下：
# 1，使用f005velocityDiscre.py运行后返回的数据bus_data
# 2，定义变量save_path用于指定保存文件的路径和文件名，默认值为'/Users/mr.tao/mycode/VDTN/deliveryLevel_calculate/x1x6.txt'
# 3，为bus_data新创建一列，名为deliveryLevel；删除以下列：time，busID，longitude，latitude，velocity
# 4，将数据存入到save_path中(保存方式：.to_csv(save_path, index=False, header=False, sep=','))

# 我调整了以下f006lastProcess.py的需求，请根据以下要求作修改：
# 1，使用f005velocityDiscre.py运行后返回的数据bus_data
# 2，定义变量save_path用于指定保存文件的路径和文件名，默认值为'/Users/mr.tao/mycode/VDTN/deliveryLevel_calculate/x1x6.txt'；定义另一个变量save_path_before也用来指定保存文件的路径和文件名，默认值为'/Users/mr.tao/mycode/VDTN/deliveryLevel_calculate/x1x6All.txt'
# 3，为bus_data新创建一列，名为deliveryLevel；
# 4, 调整bus_data列的排序，使其为：regionCode，timeSlot，moveDirection，contactInterval，velocityLevel，pathID，deliveryLevel，time，busID，longitude，latitude，velocity
# 5，将数据存入到save_path_before中(保存方式：.to_csv(save_path, index=False, header=False, sep=','))
# 6,删除以下列：time，busID，longitude，latitude，velocity
# 7,将数据存入到save_path中(保存方式：.to_csv(save_path, index=False, header=False, sep=','))

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






