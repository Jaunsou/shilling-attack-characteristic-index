import pandas as pd
import numpy as np
df = pd.read_csv('Scoring_Matrices.csv',index_col=0)
print(df)

#####计算平均评分向量长度
sum_count = 0
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

    count = rating_count[1] + rating_count[2] + rating_count[3] + rating_count[4] + rating_count[5]
    sum_count = sum_count+count
avg_count = sum_count / 943

#######计算分母
denominator = 0 #公式分母
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
    count = rating_count[1] + rating_count[2] + rating_count[3] + rating_count[4] + rating_count[5]
    denominator = denominator + (count - avg_count)**2

#######计算并保存最终结果
data = np.zeros((943,1))
df1 = pd.DataFrame(data)
df1 = df1.rename(columns={0:'LengthVar'})
LengthVar = 0
tag = 0
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

    count = rating_count[1] + rating_count[2] + rating_count[3] + rating_count[4] + rating_count[5]
    LengthVar = (count - avg_count) / denominator
    df1.iloc[tag, 0] = LengthVar
    tag = tag + 1
    print('用户',tag,'评分向量的长度变化',LengthVar)
# print(df1)
# df1.to_csv(r'c:\Users\20795\PycharmProjects\movielens\\LengthVar.csv')