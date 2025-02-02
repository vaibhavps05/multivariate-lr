import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('home.txt', names=['size', 'bedroom', 'price'])

# print(df.head())

# Feature Normalization
df = (df - df.mean()) / df.std()

# print(df.head())

# Create a matrix and set hyperparameters

# setting matrix
X = df.iloc[:, 0:2]
ones = np.ones([X.shape[0], 1])
X = np.concatenate((ones, X), axis=1)

y = df.iloc[:, 2:3].values
theta = np.zeros([1, 3])

# set hyperparameters
alpha = 0.01
iters = 1000

# Crete cost function

#compute cost
def computeCost(X, y, theta):
    tobesummed = np.power(((X @ theta.T) - y), 2)
    return np.sum(tobesummed) / (2 * len(X))

# Create gradient descent function

#gradient descent
def gradientDescent(X, y, theta, alpha, iters):
    cost = np.zeros(iters)
    for i in range(iters):
        theta = theta - (alpha/len(X)) * np.sum(X * (X @ theta.T - y), axis=0)
        cost[i] = computeCost(X, y, theta)
    
    return theta, cost

# running the gradient descent and cost function
g, cost = gradientDescent(X, y, theta, alpha, iters)
print(g)

finalCost = computeCost(X, y, g)
print(finalCost)

# Plot the cost function
fig, ax = plt.subplots()
ax.plot(np.arange(iters), cost, 'r')
ax.set_xlabel('Iterations')
ax.set_ylabel('Cost')
ax.set_title('Error vs. Training Epoch')