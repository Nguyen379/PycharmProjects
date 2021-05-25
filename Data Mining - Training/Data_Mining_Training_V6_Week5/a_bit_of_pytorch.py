import torch
from torchvision import transforms, datasets
import matplotlib.pyplot as plt
import torch.utils.data
from collections import Counter
import torch.nn as nn
import torch.nn.functional as F

# x = torch.Tensor([4, 3])
# y = torch.Tensor([2, 5])
# print(x * y)
# x = torch.zeros([2, 5])
# print(x.shape)
# y = torch.rand([2, 5])
# print(y, y.shape)
# y = y.view([1, 10])
# print(y)
# print("Testing")
train = datasets.MNIST("", train=True, transform=transforms.Compose([transforms.ToTensor()]))
test = datasets.MNIST("", train=False, transform=transforms.Compose([transforms.ToTensor()]))
trainset = torch.utils.data.DataLoader(train, batch_size=10, shuffle=True)
testset = torch.utils.data.DataLoader(test, batch_size=10, shuffle=True)

# first batch of 10 images
images, labels = [], []
for n in trainset:
    b_images, b_labels = n
    images.extend(b_images)
    labels.extend(b_labels)
images = [image.view([28, 28]) for image in images]
labels = [int(label) for label in labels]
print(Counter(labels))


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(28 * 28, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 64)
        self.fc4 = nn.Linear(64, 10)


net = Net()
print(net)
