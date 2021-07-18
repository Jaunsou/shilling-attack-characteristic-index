# shilling-attack-characteristic-index
由于攻击者对系统中用户评分数据库的知识获取度不高，或者出于对攻击成
本的考虑，使得绝大多数的托攻击行为的知识水平较低。这样攻击者在制造攻击
概貌时与真实用户对项目评分的方式上一定会存在差异，反应到用户概貌中则会
表现为真实用户与攻击用户的评分向量一定会在某种特征上存在差别。一些学者
根据这种现象提出一些经典的特征指标，从不同的方面来刻画评分向量
的差异性。经典的特征指标有：用户 k 近邻的平均相似度（DegSim），评分向量
长度变化（LengthVar），评分平均偏移度 RDMA（Rating Deviation from Mean 
Agreement），加权的评分平均偏移度 WDMA（Weighted Deviation from Mean 
Agreement），评分偏移度 WDA（Weighted Degree of Agreement），评分方差均值
MeanVar（Mean Variance），目标项目评分偏移度 FMTD（Filler Mean Target 
Difference），项目关注度 TMF（Target Model Focus）。
