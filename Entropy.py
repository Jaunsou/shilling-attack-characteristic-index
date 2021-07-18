import pandas as pd
import numpy as np
import math
file = open("u_sorted.csv", 'r',
            encoding='UTF-8')
data = {}  # # 存放每位用户评论的电影和评分
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

####计算用户评分向量熵
data = np.zeros((943,1))
df1 = pd.DataFrame(data)
df1 = df1.rename(columns={0:'Entropy'})
tag = 0
for index,row in df.iterrows():
    row_count = df.loc[index].value_counts()#统计每行元素的值的个数
    if '1' not in row_count.index:
        row_count['1'] = 0
    if '2' not in row_count.index:
        row_count['2'] = 0
    if '3' not in row_count.index:
        row_count['3'] = 0
    if '4' not in row_count.index:
        row_count['4'] = 0
    if '5' not in row_count.index:
        row_count['5'] = 0

    rating_count = row_count[1:]
    rating_count = rating_count.sort_index()
    sum_count = rating_count['1']+rating_count['2']+rating_count['3']+rating_count['4']+rating_count['5']
    rating_count = rating_count.sort_index()
    # print(rating_count)
    Entropy = 0
    for i in range(0,5):
        if rating_count[i] == 0:
            continue
        Entropy = Entropy + (rating_count[i] / sum_count) * math.log2(rating_count[i] / sum_count)
    df1.iloc[tag,0] = -Entropy
    tag = tag + 1

    print('用户',tag,'评分向量的熵',-Entropy)
# print(df1)
# df1.to_csv(r'c:\Users\20795\PycharmProjects\movielens\\Entropy.csv')#保存

