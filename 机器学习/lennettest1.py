import torch
from torch.autograd import Variable
import torch.nn as nn
import torchvision

"""MNIST数据集"""
train_dataset = torchvision.datasets.MNIST("dataset", train=True,
                                           transform=torchvision.transforms.ToTensor(), download=True)
test_dataset = train_dataset

# DataLoader
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                           batch_size=128,
                                           shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                          batch_size=100,
                                          shuffle=False)

"""LetNet-5"""


class LeNet5(nn.Module):
    def __init__(self):
        super(LeNet5, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, kernel_size=5, padding=2)  # padding = 2, 28+2+2=32
        self.conv2 = nn.Conv2d(6, 16, kernel_size=5)
        self.pool = nn.MaxPool2d(2)
        self.relu = nn.ReLU()
        self.fc1 = nn.Linear(400, 120)  # 400=16*5*5
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)
        self.softmax = nn.Softmax()

    def forward(self, x):
        in_size = x.size(0)
        out = self.relu(self.pool(self.conv1(x)))
        out = self.relu(self.pool(self.conv2(out)))
        out = out.view(in_size, -1)
        out = self.relu(self.fc1(out))
        out = self.relu(self.fc2(out))
        out = self.fc3(out)
        return self.softmax(out, )


model = LeNet5()

# 损失函数：交叉熵损失
loss_func = torch.nn.CrossEntropyLoss()

# 定义优化器
opt = torch.optim.Adam(model.parameters(), lr=0.001)


def train(epoch):
    model.train()
    for batch_index, (data, target) in enumerate(train_loader):
        data, target = Variable(data), Variable(target)
        opt.zero_grad()  # backward前梯度清零
        output = model(data)
        loss = loss_func(output, target)
        # 误差反向传播
        loss.backward()
        # 参数更新
        opt.step()
        if batch_index % 20 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_index * len(data), len(train_loader.dataset),
                       100. * batch_index / len(train_loader), loss.item()))


def test():
    model.eval()
    test_loss = 0
    correct = 0
    for data, target in test_loader:
        data, target = Variable(data, volatile=True), Variable(target)
        output = model(data)
        # 叠加loss
        test_loss += loss_func(output, target).item()
        # 最大概率预测结果标签
        pred = torch.max(output.data, 1)[1]
        correct += pred.eq(target.data.view_as(pred)).cpu().sum()
        test_loss /= len(test_loader.dataset)

        print('Test set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)'.format(
            test_loss, correct, len(test_loader.dataset),
            100. * correct / len(test_loader.dataset)))


# 迭代10轮后测试
for epoch in range(1, 11):
    train(epoch)

test()