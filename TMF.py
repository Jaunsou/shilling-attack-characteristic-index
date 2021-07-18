import pandas as pd
import numpy as np

df = pd.read_csv('Scoring_Matrices.csv',index_col=0)
print(df)
#############每个用户的最大评分项S_Max,每个用户的最大评分项个数S_Max_count
S_Max = []
S_Max_count = []
for i in range(1,944):
    s = df.loc[i,:]
    s_max = s[s == s.max()].index
    S_Max.append(s_max)
for i in range(0,943):
    S_Max_count.append(len(S_Max[i]))
# for i in range(0, 943):
#     for j in range (0,len(S_Max[i])):
#          print(S_Max[i][j])
df1 = pd.read_csv('Scoring_Matrices.csv',index_col=0)
df1 = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)#评分矩阵的转置
# print(df1)
################每个项的最大评分用户U_Max,每个项的最大评分用户个数U_Max_count
U_Max = []
U_Max_count = []
for i in range(1,1683):
    u = df1.loc[str(i),:]
    u_max = u[u == u.max()].index
    U_Max.append(u_max)
for i in range(0,1682):
    U_Max_count.append(len(U_Max[i]))

####################计算目标项目关注度TMF
data = np.zeros((943,1))
df2 = pd.DataFrame(data)
df2 = df2.rename(columns={0:'TMF'})
TMF = []
for i in range(0,943):
    # print(S_Max[i])
    T = []
    for j in range(0,len(S_Max[i])):
        k = int(S_Max[i][j])
        # print(k)
        # print(U_Max[k-1])
        Ijmax = U_Max_count[k - 1]
        sum = 0
        for index in U_Max[k - 1]:
            sum = sum + S_Max_count[index - 1]
        T.append(Ijmax / sum)
    print('用户',i+1,'目标项目关注度',max(T))
    TMF.append(max(T))
    df2.iloc[i, 0] = max(T)
# print(df2)
# df2.to_csv(r'c:\Users\20795\PycharmProjects\movielens\\TMF.csv')
