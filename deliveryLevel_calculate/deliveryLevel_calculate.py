import pandas as pd
from mytxt.train import train  # 导入train.py中的train函数

def main():
    # 定义变量
    file_path = '/Users/mr.tao/mycode/VDTN/deliveryLevel_calculate/x1x6All.txt'
    save_path = '/Users/mr.tao/mycode/VDTN/deliveryLevel_calculate/x1x7All.txt'

    # 读取数据
    column_names = [
        "regionCode", "timeSlot", "moveDirection", "contactInterval", 
        "velocityLevel", "pathID", "deliveryLevel", "time", 
        "busID", "longitude", "latitude", "velocity"
    ]
    bus_data = pd.read_csv(file_path, names=column_names, sep=',')

    # 调用train函数
    result_data = train(bus_data)

    # 保存结果
    result_data.to_csv(save_path, index=False, header=False, sep=',')

if __name__ == "__main__":
    main()
