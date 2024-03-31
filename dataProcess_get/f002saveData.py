# 功能：将list数据保存为原始数据集的格式存入到新建txt中
import pandas as pd


def save_data(data, save_path):
    # 输入：list变量，保存路径（包含文件名）

    # 合并list中的所有 DataFrame 对象
    merged_data = pd.concat(data, ignore_index=True)
    # 保存
    merged_data.to_csv(save_path, index=False, header=False, sep=',')




