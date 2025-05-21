# %%
import torch
from torch import nn


# %%
class neural_network(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(6, 50)
        self.layer2 = nn.Linear(50,100)        
        self.layer3 = nn.Linear(100,150)
        self.layer4 = nn.Linear(150,1)
        self.activation = nn.ReLU()
        self.drop = nn.Dropout(0.2)
        
    def forward(self,x):
        x = self.layer1(x)
        x = self.activation(x)
        x = self.layer2(x)
        x = self.activation(x)
        x = self.layer3(x)
        x = self.activation(x)
        x = self.drop(x)
        x = self.layer4(x)
        
        return x 
        

# %%
