import csv
import numpy as np
import torch
import torch.nn as nn

# Set random seed
torch.manual_seed(0)

# Specify the path to the CSV file
csv_file = 'Sierpinski_1000.csv'

# Read the data from the CSV file
data = []
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

# Convert the data to a NumPy array
data = np.array(data, dtype=float)

# Split the data into training and test sets
train_data = data[:40]
validation_data = data[6:16]
test_data = data[-6:]

# Convert the data to PyTorch tensors
X_train = torch.from_numpy(train_data[:, :-1]).float()
y_train = torch.from_numpy(train_data[:, -1]).float()
X_test = torch.from_numpy(test_data[:, :-1]).float()
y_test = torch.from_numpy(test_data[:, -1]).float()
X_validation = torch.from_numpy(validation_data[:, :-1]).float()
y_validation = torch.from_numpy(validation_data[:, -1]).float()

class ESN(nn.Module):
    def __init__(self, input_size, hidden_size, reservoir_size):
        super(ESN, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.reservoir_size = reservoir_size
        self.input_weights = nn.Linear(input_size, reservoir_size, bias=False)
        self.hidden_weights = nn.Linear(reservoir_size, reservoir_size, bias=True)
        self.output_weights = nn.Linear(reservoir_size, hidden_size, bias=False)

    def forward(self, x):
        x = torch.tanh(self.input_weights(x))
        x = torch.tanh(self.hidden_weights(x))
        x = self.output_weights(x)
        return x


input_size = X_train.shape[1]
hidden_size = 1
reservoir_size = 1

#best fits hs=1, rs=510, epoch 4

model = ESN(input_size, hidden_size, reservoir_size)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

for epoch in range(10):
    # Forward pass
    predictions = model(X_train)

    # Reshape y_train to match the shape of predictions
    y_train_reshaped = y_train.view(-1, 1)

    # Compute the loss
    loss = nn.MSELoss()(predictions, y_train_reshaped)

    # Zero gradients, perform a backward pass, and update the weights
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Forward pass on validation set
validation_predictions = model(X_validation)
y_validation_reshaped = y_validation.view(-1, 1)
validation_loss = nn.MSELoss()(validation_predictions, y_validation_reshaped)

# Compute and print the difference between the train and validation loss
train_loss = loss.item()
val_loss = validation_loss.item()
diff = train_loss - val_loss
print("Epoch: ", epoch, "Train Loss: ", train_loss, "Validation Loss: ", val_loss, "Difference (negative = overfit) : ", diff)
#a positive difference means that the model is overfitting, and a negative difference means that the model is underfitting


# Reshape y_test to match the shape of test_predictions
y_test_reshaped = y_test.view(-1, 1)

test_predictions = model(X_test)
mse = nn.MSELoss()(test_predictions, y_test_reshaped)
print("MSE: ", mse.item())

#MAE
mae = nn.L1Loss()(test_predictions, y_test_reshaped)
print("MAE: ", mae.item())
