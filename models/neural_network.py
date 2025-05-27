# %%
import torch
from torch import nn

# %%
class neural_network(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(103, 206)
        self.layer2 = nn.Linear(206,412)        
        self.layer3 = nn.Linear(412,824)
        self.layer4 = nn.Linear(824,412)
        self.layer5 = nn.Linear(412, 206)
        self.layer6 = nn.Linear(206, 103)
        self.layer7 = nn.Linear(103, 50)
        self.layer8 = nn.Linear(50,1)
        self.activation = nn.ReLU()
        self.drop = nn.Dropout(0.1)
        
    def forward(self,x):
        x = self.layer1(x)
        x = self.activation(x)
        x = self.drop(x)

        x = self.layer2(x)
        x = self.activation(x)
        x = self.drop(x)

        x = self.layer3(x)
        x = self.activation(x)
        x = self.drop(x)
        
        x = self.layer4(x)
        x = self.activation(x)
        x = self.drop(x)
        
        x = self.layer5(x)
        x = self.activation(x)
        x = self.drop(x)
        
        x = self.layer6(x)
        x = self.activation(x)
        x = self.drop(x)
        
        x = self.layer7(x)
        x = self.activation(x)
        x = self.drop(x)
        
        x = self.layer8(x)
        
        return x 
        

# %%
