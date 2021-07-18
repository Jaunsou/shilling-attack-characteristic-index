import pandas as pd
import numpy as np
import math
#############################统计每个用户的总评分次数
df = pd.read_csv('Scoring_Matrices.csv',index_col=0)
# print(df)
S_count = []  #将评分总数和平均分存入数组
for index,row in df.iterrows():
    row_count = df.loc[index].value_counts()#统计每行元素的值的个数
    if 1 not in row_count.index:
        row_count[1] = 0
    if 2 not in row_count.index:
        row_count[2] = 0
    if 3 not in row_count.index:
        row_count[3] = 0
    if 4 not in row_count.index:
        row_count[4] = 0
    if 5 not in row_count.index:
        row_count[5] = 0
    rating_count = row_count[1:]
    count = rating_count[1] + rating_count[2] + rating_count[3] + rating_count[4]+ rating_count[5]
    # print(rating_count,count)
    S_count.append(count)

###################每个用户的最大评分项S_Max,每个用户的最大评分项个数S_Max_count
df = pd.read_csv('Scoring_Matrices.csv',index_col=0)
S_Max = []
S_Max_count = []
for i in range(1,944):
    s = df.loc[i,:]
    s_max = s[s == s.max()].index
    S_Max.append(s_max)
for i in range(0,943):
    S_Max_count.append(len(S_Max[i]))
###################每个用户的其他评分项（除最大评分）S_else,每个用户的其他评分项（除最高分）个数S_else_count
df = pd.read_csv('Scoring_Matrices.csv', index_col=0)
S_Else = []
S_Else_count = []
for i in range(1, 944):
    s = df.loc[i, :]
    s_else = s[(s != s.max()) & (s != 0)].index
    S_Else.append(s_else)
for i in range(0, 943):
    S_Else_count.append(len(S_Else[i]))
# print(S_Else_count)
# ##################计算用户的其他评分项目（除最高分）个数,Else_count
# Else_count = []
# for i in range(0,943):
#     # print(S_count[i],'-',S_Max_count[i],i+1)
#     Else_count.append(S_count[i] - S_Max_count[i])
# print(Else_count)
###################计算评分最高项目平均分，并保存入数组
df1 = pd.read_csv('Scoring_Matrices.csv',index_col=0)
Highest_Avg = []
for i in range(0,943):
    high = 0
    for j in range(0,len(S_Max[i])):
        k = S_Max[i][j]
        # print(k ,i)
        high = high + df1.iloc[i,int(k)-1]
    highest_avg = high / S_Max_count[i]
    Highest_Avg.append(highest_avg)
# print(Highest_Avg)

###################计算其他项目平均分，并保存入数组
df2 = pd.read_csv('Scoring_Matrices.csv',index_col=0)
Else_Avg = []
for i in range(0,943):
    selse = 0
    for j in range(0,len(S_Else[i])):
        k = S_Else[i][j]
        # print(k ,i)
        selse = selse + df2.iloc[i,int(k)-1]
    else_avg = selse / S_Else_count[i]
    Else_Avg.append(else_avg)
# print(Else_Avg)
###################计算每个用户目标项目评分偏移度FMTD，并保存
data = np.zeros((943,1))
df3 = pd.DataFrame(data)
df3 = df3.rename(columns={0:'FMTD'})
for i in range (0,943):
    FMTD = math.fabs(Highest_Avg[i] - Else_Avg[i])
    print('用户', i + 1, '目标项目评分偏移度', FMTD)
    df3.iloc[i, 0] = FMTD
# print(df3)
# df3.to_csv(r'c:\Users\20795\PycharmProjects\movielens\\FMTD.csv')