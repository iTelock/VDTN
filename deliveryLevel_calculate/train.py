
import pandas as pd
import random
from oneTimeTrain import oneTimeTrain
from rewardCalculate import calculate_and_update_rewards  

# 定义变量 step，代表迭代次数
step = 1000

def train(bus_data):
    unique_busIDs = bus_data['busID'].unique()  # 获取所有不重复的busID值
    
    for _ in range(step):
        # 随机挑选两个不同的busID值
        sNode, dNode = random.sample(list(unique_busIDs), 2)
        
        # 调用oneTimeTrain函数开始单次训练
        path = oneTimeTrain(bus_data, sNode, dNode)
        bus_data = calculate_and_update_rewards(path, bus_data)
    
    return bus_data  # 返回最终的bus_data

if __name__ == "__main__":
    # 测试train函数是否正常
    test_data_path = '/Users/mr.tao/mycode/VDTN/deliveryLevel_calculate/x1x6All.txt'
    test_data = pd.read_csv(test_data_path, sep=',', header=None)
    test_data.columns = ['regionCode', 'timeSlot', 'moveDirection', 'contactInterval', 'velocityLevel', 'pathID', 'deliveryLevel', 'time', 'busID', 'longitude', 'latitude', 'velocity']
    
    result_data = train(test_data)
    print(result_data.head())  # 打印结果数据的前五行以验证




