import pandas as pd
from f001regionCodeDiscre import process_data
from f002timeSlotDiscre import assign_time_slot
from f003moveDirectionDiscre import assign_move_direction
from f004contactIntervalDiscre import assign_contact_interval
from f005velocityDiscre import process_velocity
from f006lastProcess import final_process

# 指定数据集文件路径
file_path = '/Users/mr.tao/mycode/VDTN/dataProcess_get/theMostData.txt'

# 处理后数据保存位置
save_path='/Users/mr.tao/mycode/VDTN/deliveryLevel_calculate/x1x6.txt'
save_path_before='/Users/mr.tao/mycode/VDTN/deliveryLevel_calculate/x1x6All.txt'

# 读取数据函数
def read_data():
    # 定义列名
    column_names = ["date", "time", "busID", "pathID", "longitude", "latitude", "velocity"]
    
    # 读取数据
    data = pd.read_csv(file_path, sep=',', header=None, names=column_names)
    
    # 将数据转换为字典列表
    bus_data = data.to_dict('records')
    
    return bus_data

# 读取数据
bus_data = read_data()

# 创建区域码并离散化
bus_data = process_data(bus_data)

# 创建时间段并离散化
bus_data = assign_time_slot(bus_data)

# 创建并计算运动方向
bus_data = assign_move_direction(bus_data)

# 创建并计算平均相遇间隔时间
bus_data = assign_contact_interval(bus_data)

# 创建并计算速度等级velocityLevel
bus_data = process_velocity(bus_data)

# 处理为x1~x7的格式并保存数据
final_process(bus_data, save_path, save_path_before)

print(bus_data[0])
print()
print(bus_data[38])
print()
print(bus_data[438])
print()
print(bus_data[3473])
print()
print(bus_data[6173])
print()
print("bus_data 的类型:", type(bus_data))
print("theMostData.txt中的数据量:58000")
print("目前bus_data中的元素数量:", len(bus_data))
# bus_data = pd.DataFrame(bus_data)
# print(bus_data)


# 最终数据格式（x1x6.txt）
# regionCode，区域码
# timeSlot，时间段
# moveDirection，运动方向
# contactInterval，平均相遇等级（越低遇到的节点越多）
# velocityLevel，速度等级
# pathID，路线
# deliveryLevel，交付等级
