# 23 二分类交叉熵损失函数
# L(w) = -加和(真实标签*ln(预测概率)+(1-真实标签)*ln(1-预测概率))

极大似然估计Maximum Likelihood Estimate MLE
   
# tensor实现二分类交叉熵损失函数
import torch
# Loss = -(y*ln(sigma)+(1-y)*ln(1-sigma)
# y = 真实标签
# sigma = 预测函数（需要X，w）
# m = 样本量
m = 3*pow(10,3)
torch.random.manual_seed(420)
X = torch.rand((m,4),dtype=torch.float32)
w = torch.rand((4,1),dtype=torch.float32)
y = torch.randint(low=0,high=2,size=(m,1),dtype=torch.float32)
zhat = torch.mm(X,w)
sigma = torch.sigmoid(zhat)
sigma.shape

single_loss = -(y*torch.log(sigma)+(1-y)*torch.log(1-sigma))
total_loss = -torch.sum(y*torch.log(sigma)+(1-y)*torch.log(1-sigma))
average_loss = -(1/m)*torch.sum(y*torch.log(sigma)+(1-y)*torch.log(1-sigma))

# pytorch实现二分类交叉熵损失函数
# class BCEWithLogitsLoss内置了sigmoid函数与交叉熵函数，会自动计算sigmoid值，所以需要输入zhat与真实标签
# class BCELoss没有sigmoid函数，需要输入sigma和真实标签

import torch.nn as nn
criterion = nn.BCELoss()
loss = criterion(sigma, y)
criterion2 = nn.BCEWithLogitsLoss(zhat, y)
# reduction参数 (reduction = "mean"/"sum"/"none")默认求均值

# 24 多分类交叉熵损失函数
# one-hot coding独热编码
# 求和ln（预测概率）
# 通过nn.LogSoftmax(=log+sigmoid)+负对数似然函数 NLLLoss实现 
import torch
import torch.nn as nn
m = 3*pow(10,3)
torch.random.manual_seed(420)
X = torch.rand((m,4),dtype=torch.float32)
w = torch.rand((4,3),dtype=torch.float32)
y = torch.randint(low=0,high=3,size=(m,),dtype=torch.float32)
zhat = torch.mm(X,w)
logsm = nn.LogSoftmax(dim=1)
logsigma = logsm(zhat)
criterion = nn.NLLLose()
criterion(logsigma, y.long())

# 直接调用nn.CrossEntropyLoss，包含了sigmoid，可以直接放入zhat
criterion = nn.CrossEntropyLoss()
criterion(zhat,y.long())

# 25 神经网络的优化
# w(t+1) = w(t) - lr*w的偏导数 ->每一个权重w1、w2....的偏导数

# 26 反向传播
# 只需要一次正向传播，储存传播中计算的中间值，损失函数链式求导后的公式所需代入得值都得到了
