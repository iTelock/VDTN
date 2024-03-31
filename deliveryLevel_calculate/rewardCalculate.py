def find_shortest_path(paths):
    # 选择路径最短的一条
    shortest_length = float('inf')
    shortest_path = None
    for path in paths:
        if len(path) < shortest_length:
            shortest_length = len(path)
            shortest_path = path
    return shortest_path

def calculate_reward(shortPath):
    # 根据路径长度计算每个节点的奖励值
    num = len(shortPath)
    rewards = [(2*600*order)/(num*(num-1)) for order in range(1, num+1)]
    return rewards

def update_deliveryLevel(bus_data, shortPath, rewards):
    # 更新bus_data中的deliveryLevel
    for i, node in enumerate(shortPath):
        reward = rewards[i]
        if reward <= 50:
            deliveryLevel = 1
        elif reward <= 100:
            deliveryLevel = 2
        elif reward <= 150:
            deliveryLevel = 3
        elif reward <= 200:
            deliveryLevel = 4
        elif reward <= 300:
            deliveryLevel = 5
        elif reward <= 500:
            deliveryLevel = 6
        else:
            deliveryLevel = 7
        
        # 更新bus_data中对应节点的deliveryLevel
        for data in bus_data:
            if data[8] == node[8]:  # 假设busID能唯一标识节点
                data[6] = deliveryLevel
                break

def calculate_and_update_rewards(paths, bus_data):
    # 计算奖励值并更新bus_data
    shortPath = find_shortest_path(paths)
    if not shortPath:
        print("路径为空")
        return
    
    rewards = calculate_reward(shortPath)
    update_deliveryLevel(bus_data, shortPath, rewards)
    print("路径已更新")

