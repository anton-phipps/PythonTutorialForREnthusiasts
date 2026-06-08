# Block 1
import torch

# Create a tensor from a list
x = torch.tensor([1, 2, 3, 4])

# Create a random tensor
y = torch.randn(3, 3) # 3x3 matrix

# Matrix multiplication
result = torch.matmul(y, y.T)

# Block 2
x = torch.tensor([2.0], requires_grad=True)
y = x**2 + 5

y.backward() # Compute gradient
print(x.grad) # dy/dx = 2x = 4.0

# Block 3
import torch.nn as nn

class SimpleClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(SimpleClassifier, self).__init__()
        # Layers
        self.fc1 = nn.Linear(input_size, hidden_size) 
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)
    
    def forward(self, x):
        # The data flow
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

model = SimpleClassifier(4, 10, 3)
print(model)

# Block 4
import torch
import torch.nn as nn

# Dummy data for the training loop example
inputs = torch.randn(10, 4)
labels = torch.randint(0, 3, (10,))

# Block 5
# Pseudo-code for a training loop (now executable!)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
criterion = nn.CrossEntropyLoss()

for epoch in range(10): # Reduced epochs for testing
    # 1. Forward
    outputs = model(inputs)
    loss = criterion(outputs, labels)
    
    # 2. Backward
    optimizer.zero_grad() # Clear old gradients
    loss.backward()
    
    # 3. Step
    optimizer.step()

