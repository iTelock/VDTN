import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import BayesianEstimator, K2Score, ParameterEstimator
from sequence import GeneticAlgorithm
from pgmpy.inference import BeliefPropagation

# 加载数据
file_path = '/Users/mr.tao/mycode/VDTN/deliveryLevel_calculate/x1x7All.txt'
save_path = ''
bus_data = pd.read_csv(file_path)
print("数据加载完毕。")

# 定义评分函数(需要修改K2Score引入GA)
score = K2Score(data=bus_data)

ga = GeneticAlgorithm(data=bus_data, scoring_method=score)
best_model_structure_edges = ga.run()  # 假设run方法返回最优网络结构的边列表

# 创建贝叶斯模型
model = BayesianModel(best_structure_edges)

# 参数学习
model.fit(bus_data, estimator=BayesianEstimator, prior_type="BDeu")  # 使用BDeu先验进行参数估计
print("模型参数学习完成。")

# 推理部分
# 创建团树（Junction Tree）推理对象
bp = BeliefPropagation(model)

# 执行查询（示例）
# 假设我们想知道给定其他变量情况下，'deliveryLevel'的概率分布
query_vars = ['deliveryLevel']  # 查询变量
evidence = {'regionCode': 1, 'timeSlot': 2}  # 已知证据
result = bp.query(variables=query_vars, evidence=evidence)

print("查询结果：")
print(result)






