import pandas as pd
import numpy as np
file = open("u_sorted.csv", 'r',
            encoding='UTF-8')
data = {}  # # 存放每位用户评论的电影和评分
###########################生成评分矩阵
for line in file.readlines()[0:100000]:
    # 注意这里不是readline()
    line = line.strip().split(',')
    # 如果字典中没有某位用户，则使用用户ID来创建这位用户
    if not line[0] in data.keys():
        data[line[0]] = {line[1]: line[2]}
    # 否则直接添加以该用户ID为key字典中
    else:
        data[line[0]][line[1]] = line[2]
df = pd.DataFrame(data).T.fillna('0')
print(df)
#########计算用户余弦相似度矩阵
data = np.zeros((943,943))
df2 = pd.DataFrame(data)
def cos_sim(a,b):
    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)
    cos = np.dot(a,b) / (a_norm * b_norm)
    return cos
for i in range(0,943):
    print('用户',i+1,'相似度')
    t1 = df.iloc[i]
    t1 = t1.values
    t1 = list(map(int, t1))
    for j in range(0,943):
        if i == j:
            continue
        t2 = df.iloc[j]
        t2 = t2.values
        t2 = list(map(int, t2))
        df2.iloc[i,j] = cos_sim(t1,t2)
# print(df2)
# # df2.to_csv(r'c:\Users\20795\PycharmProjects\movielens\\Cos_Sim.csv')#保存

#########计算用户之间的相似度，k取10
df = pd.read_csv('Cos_Sim.csv',index_col=0)
print(df)
k = 10
data = np.zeros((943,1))
df1 = pd.DataFrame(data)
df1 = df1.rename(columns={0:'Degsim'})
for i in range(0,943):
    Degsim_sum = 0
    for j in range(0,k):
        df = df.sort_values(by=str(i), ascending=False)
        Degsim_sum = Degsim_sum + df.iloc[j,i]
    Degsim = Degsim_sum / k
    df1.iloc[i, 0] = Degsim
    print("用户“,i+1,”模型与其 k(k = 10) 近邻的平均相似度",Degsim)
# df1.to_csv(r'c:\Users\20795\PycharmProjects\movielens\\Degsim.csv')#保存



