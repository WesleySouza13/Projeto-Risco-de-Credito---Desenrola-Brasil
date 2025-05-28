# %%
import torch
from torch import nn
# %%
class neural_network(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(103, 256)
        self.bn1 = nn.BatchNorm1d(256)
        self.layer2 = nn.Linear(256,128)  
        self.bn2 = nn.BatchNorm1d(128)      
        self.layer3 = nn.Linear(128,64)
        self.bn3 = nn.BatchNorm1d(64)
        self.layer4 = nn.Linear(64,1)
        self.activation = nn.LeakyReLU()
        self.drop = nn.Dropout(0.2)
        
    def forward(self,x):
        x = self.layer1(x)
        x = self.bn1(x)
        x = self.activation(x)
        x = self.drop(x)

        x = self.layer2(x)
        x = self.bn2(x)
        x = self.activation(x)
        x = self.drop(x)

        x = self.layer3(x)
        x = self.bn3(x)
        x = self.activation(x)
        x = self.drop(x)
        
        x = self.layer4(x)

        return x 
        

# %%
