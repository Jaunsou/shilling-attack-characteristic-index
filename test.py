import pandas as pd
import numpy as np
import math
df = pd.read_csv('Scoring_Matrices.csv',index_col=0)
# print(df)
############计算每个电影的平均评分
# Count = []  #将评分总数和平均分存入数组
# Avg_rating = []
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
    print(rating_count,count)
    # Count.append(count)
    # for a, b, c, d, e in np.nditer([rating_count[1], rating_count[2], rating_count[3], rating_count[4], rating_count[5]]):
    #     avg_ratings = (a + 2 * b + 3 * c + 4 * d + 5 * e) / count
    #     Avg_rating.append(avg_ratings)
# print(Count)
# print(Avg_rating)
#
#
# #############################统计每个用户的总评分次数
# df = pd.read_csv('Scoring_Matrices.csv',index_col=0)
# # print(df)
# S_count = []  #将评分总数和平均分存入数组
# for index,row in df.iterrows():
#     row_count = df.loc[index].value_counts()#统计每行元素的值的个数
#     if 1 not in row_count.index:
#         row_count[1] = 0
#     if 2 not in row_count.index:
#         row_count[2] = 0
#     if 3 not in row_count.index:
#         row_count[3] = 0
#     if 4 not in row_count.index:
#         row_count[4] = 0
#     if 5 not in row_count.index:
#         row_count[5] = 0
#     rating_count = row_count[1:]
#     count = rating_count[1] + rating_count[2] + rating_count[3] + rating_count[4]+ rating_count[5]
#     # print(rating_count,count)
#     S_count.append(count)

# ###################每个用户的其他评分项（除最大评分）S_else,每个用户的最大评分项个数S_else_count
# df = pd.read_csv('Scoring_Matrices.csv',index_col=0)
# S_else = []
# S_else_count = []
# for i in range(1,944):
#     s = df.loc[i,:]
#     s_else = s[s != (s.max() and 0)].index
#     S_else.append(s_else)
#
# for i in range(0,943):
#     S_else_count.append(len(S_else[i]))
# ##################计算用户的其他评分项目（除最高分）个数,Else_count
# Else_count = []
# for i in range(0,943):
#     # print(S_count[i],'-',S_Max_count[i],i+1)
#     Else_count.append(S_count[i] - S_Max_count[i])
# # print(Else_count)
#
# ##################计算属性评分偏移度的平方，存入数组
#
# df1 = pd.read_csv('Scoring_Matrices.csv',index_col=0)
# # print(S_Max)
# WDA_Square = []
# for i in range(0,943):
#     W = 0
#     for j in range(0,1682):
#         if j in S_Max[i]:
#             continue
#         if df1.iloc[i,j] == 0:
#             continue
#         w = (df1.iloc[i,j] - Avg_rating[j])**2
#         W = W + w
#     WDA_Square.append(W)
#
# ###################计算FMV，并保存
# data = np.zeros((943,1))
# df2 = pd.DataFrame(data)
# df2 = df2.rename(columns={0:'FMV'})
# for i in range(0,943):
#     FMV = WDA_Square[i] / Else_count[i]
#     print('用户',i + 1,'评分方差均值',FMV)
#     df2.iloc[i, 0] = FMV
# # print(df2)
# df2.to_csv(r'c:\Users\20795\PycharmProjects\movielens\\FMV.csv')





# for index,row in df1.iterrows():
#     row_count = df1.loc[index].value_counts()#统计每行元素的值的个数j
#     if 1 not in row_count.index:
#         row_count[1] = 0
#     if 2 not in row_count.index:
#         row_count[2] = 0
#     if 3 not in row_count.index:
#         row_count[3] = 0
#     if 4 not in row_count.index:
#         row_count[4] = 0
#     if 5 not in row_count.index:
#         row_count[5] = 0
#     rating_count = row_count[1:]
#     count = rating_count[1] + rating_count[2] + rating_count[3] + rating_count[4] + rating_count[5]
#
#     MeanVar = WDA_Square[index-1] / (count - 1)
#     print('用户',index,'评分方差均值',MeanVar)
#     df2.iloc[index - 1, 0] = MeanVar
# print(df2)
# df2.to_csv(r'c:\Users\20795\PycharmProjects\movielens\\MeanVar.csv')







# print(U_Max_count[1681])
# print(U_Max)
# for i in range(0,1682):
#     for j in range (0,len(U_Max[i])):
#          print(U_Max[i][j])

# # 获得 第1 行
# s1 = df.loc[943,:]
#
# # 获得每行中最大值的索引，可能有多个
# s1_argmax = s1[s1 == s1.max()].index
# print(s1_argmax)
# # 随机从中获取一个索引 choose 1 index
# s1_argmax = np.random.choice(s1_argmax)
# print(s1_argmax)

############计算每个电影的平均评分
# for index,row in df.iterrows():
#     row_count = df.loc[index].value_counts()#统计每行元素的值的个数
#     if 1 not in row_count.index:
#         row_count[1] = 0
#     if 2 not in row_count.index:
#         row_count[2] = 0
#     if 3 not in row_count.index:
#         row_count[3] = 0
#     if 4 not in row_count.index:
#         row_count[4] = 0
#     if 5 not in row_count.index:
#         row_count[5] = 0
#     rating_count = row_count[1:]
#     count = rating_count[1] + rating_count[2] + rating_count[3] + rating_count[4] + rating_count[5]
#     print(rating_count,count)