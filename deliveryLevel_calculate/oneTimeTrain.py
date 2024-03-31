import pandas as pd
from math import radians, cos, sin, asin, sqrt

# Haversine公式计算两点间距离
def haversine(lon1, lat1, lon2, lat2):
    """
    计算两点间的距离（单位：公里）
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位公里
    return c * r

# 单次计算
def oneTimeTrain(bus_data, sNode, dNode, _range=1, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    # 添加起始节点
    visited.add(tuple(sNode))

    # 验证两个节点的timeSlot是否相同，如果不同，则视为距离超出范围
    if sNode[1] != dNode[1]:
        return []  # 返回空列表表示无法连接
    
    # 计算起始节点和目标节点之间的距离
    dist = haversine(sNode[9], sNode[10], dNode[9], dNode[10])
    if dist <= _range:
        # 如果距离在范围内，直接添加目标节点并返回路径
        return [path + [sNode, dNode]]
    
    # 如果距离超出范围，寻找临近的节点
    temp_paths = []
    for node in bus_data:
        if tuple(node) not in visited:
            temp_dist = haversine(sNode[9], sNode[10], node[9], node[10])
            if temp_dist <= _range:
                # 对于每个临近节点，递归搜索路径
                new_visited = visited.copy()
                new_visited.add(tuple(node))
                if len(path) + 1 < 5:  # 确保路径长度不超过5
                    sub_paths = oneTimeTrain(bus_data, node, dNode, _range, path + [sNode], new_visited)
                    if sub_paths:  # 如果找到子路径，添加到临时路径列表
                        temp_paths.extend(sub_paths)
    return temp_paths
