# Deep Learning with PyTorch

## Overview
Deep Learning is a subset of ML based on artificial neural networks. **PyTorch** is the most popular framework for research due to its flexibility and "Pythonic" nature.

## 1. Tensors: The Multi-dimensional Array
Tensors are the core data structure in PyTorch. They are similar to NumPy arrays but can be computed on GPUs.

```python
import torch

# Create a tensor from a list
x = torch.tensor([1, 2, 3, 4])

# Create a random tensor
y = torch.randn(3, 3) # 3x3 matrix

# Matrix multiplication
result = torch.matmul(y, y.T)
```

## 2. Autograd: The Magic of Derivatives
PyTorch automatically calculates the gradient (derivative) of a function, which is how neural networks "learn."

```python
x = torch.tensor([2.0], requires_grad=True)
y = x**2 + 5

y.backward() # Compute gradient
print(x.grad) # dy/dx = 2x = 4.0
```

## 3. Building a Neural Network
We define a network by creating a class that inherits from `nn.Module`.

```python
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
```

## 4. The Training Loop
Training involves 4 steps repeated over several "epochs":
1.  **Forward Pass:** Get predictions.
2.  **Loss Calculation:** How wrong were we?
3.  **Backward Pass:** Compute gradients.
4.  **Optimization:** Update weights to reduce loss.

```python
# Pseudo-code for a training loop
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
criterion = nn.CrossEntropyLoss()

for epoch in range(100):
    # 1. Forward
    outputs = model(inputs)
    loss = criterion(outputs, labels)
    
    # 2. Backward
    optimizer.zero_grad() # Clear old gradients
    loss.backward()
    
    # 3. Step
    optimizer.step()
```

---

## 🏆 Challenge Exercise: The Digit Recognizer (Concept)
1.  **Goal:** Imagine you are building a model to recognize handwritten digits (0-9).
2.  What should be the `input_size` if each image is 28x28 pixels? (Hint: Flatten the image).
3.  What should be the `num_classes`?
4.  Write the `__init__` and `forward` methods for a network with two hidden layers (size 128 and 64).
5.  **Bonus:** Research `torchvision.datasets.MNIST` and try to load the actual data.

---
[⬅️ Previous](01_ml_fundamentals.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](../08_advanced_topics/01_advanced_features.md)
