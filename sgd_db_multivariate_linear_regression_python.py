# -*- coding: utf-8 -*-
"""SGD_db_Multivariate_Linear_Regression_Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zY7kZQCwdOOFwv8KfEudGhHcsRSp6eQ2

# Multivariate Linear Regression
## Predicting Healthcare COVID Insurance Price from age, race, ethnicity, gender, latitude, longitude

### Import Libraries
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize

"""### Read Data"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# %matplotlib inline

#importing dataset using panda
#dataset
data = pd.read_csv('https://storage.googleapis.com/dataprep-staging-b4c6b8ff-9afc-4b23-a0d8-d480526baaa4/yz1268%40nyu.edu/jobrun/Untitled%20recipe%20%E2%80%93%204.csv/2021-08-16_23-54-42_00000000')
#to see what my dataset is comprised of
data.head()
#healthcare_coverage,age,race, ethnicity, gender, latitude, longitude,healthcare expense.
#the first column is y, the rest are all x1, x2,...xn.

data.shape

print(type(data))
#print(data.keys())
data = data.to_numpy()
print(type(data))

print(data)

data.shape

"""### Normalize Data"""

data = normalize(data, axis=0)
#data = data.values.tolist()

#print(data[0])
print('the Y value in regression model',data[:,0:1])
print('the X1 & X2 values in regression model',data[:,1:3])

"""### Seperate Data into X and Y"""

X = data[:, 1:6]
#X = data[:, 1:7] The last column is the medical expense, it is not used in the first train.
Y = data[:, 0:1]
#https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/pandas-dataframes/indexing-filtering-data-pandas-dataframes/

#X[:, 6]
data[:, ]

X.size

print(X)

"""### Visualize the Data"""

# Fixing random state for reproducibility
np.random.seed(19680801)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xs = X[:, 0]
ys = X[:, 1]
zs = Y
ax.scatter(xs, ys, zs)

ax.set_xlabel('size')
ax.set_ylabel('bedroom')
ax.set_zlabel('price')

plt.show()

"""### Hyperparameters"""

learning_rate = 0.09
max_iteration = 500

s_learning_rate = 0.06
s_max_iteration = 500

mb_learning_rate = 0.09
mb_max_iteration = 500
batch_size = 16

"""### Parameters"""

theta = np.zeros((X.shape[1]+1, 1))
#theta = np.zeros(data.shape[1])
s_theta = np.zeros((X.shape[1]+1, 1))
mb_theta = np.zeros((X.shape[1]+1, 1))

#np.zeros(data.shape[1])
X.shape[1]

theta.size

data.shape[0]

tempX = np.ones((X.shape[0], X.shape[1] + 1))
print(tempX)

tempX[:,1:].size

tempX.size

np.matmul(tempX, theta)

"""### Hypothesis"""

def h (theta, X) :
  tempX = np.ones((X.shape[0], X.shape[1] + 1))
  tempX[:,1:] = X
  return np.matmul(tempX, theta)

"""### Loss Function"""

def loss (theta, X, Y) :
  return np.average(np.square(Y - h(theta, X))) / 2

"""### Calculate Gradients"""

def gradient (theta, X, Y) :
  tempX = np.ones((X.shape[0], X.shape[1] + 1))
  tempX[:,1:] = X
  d_theta = - np.average((Y - h(theta, X)) * tempX, axis= 0)
  d_theta = d_theta.reshape((d_theta.shape[0], 1))
  return d_theta

"""### Batch Gradient Descent"""

def gradient_descent (theta, X, Y, learning_rate, max_iteration, gap) :
  cost = np.zeros(max_iteration)
  for i in range(max_iteration) :
    d_theta = gradient (theta, X, Y)
    theta = theta - learning_rate * d_theta
    cost[i] = loss(theta, X, Y)
    if i % gap == 0 :
      print ('iteration : ', i, ' loss : ', loss(theta, X, Y)) 
  return theta, cost

"""### Mini-Batch Gradient Descent"""

def minibatch_gradient_descent (theta, X, Y, learning_rate, max_iteration, batch_size, gap) :
  cost = np.zeros(max_iteration)
  for i in range(max_iteration) :
    for j in range(0, X.shape[0], batch_size):
      d_theta = gradient (theta, X[j:j+batch_size,:], Y[j:j+batch_size,:])
      theta = theta - learning_rate * d_theta
    
    cost[i] = loss(theta, X, Y)
    if i % gap == 0 :
      print ('iteration : ', i, ' loss : ', loss(theta, X, Y)) 
  return theta, cost

"""### Stochastic Gradient Descent"""

def stochastic_gradient_descent (theta, X, Y, learning_rate, max_iteration, gap) :
  cost = np.zeros(max_iteration)
  for i in range(max_iteration) :
    for j in range(X.shape[0]):
      d_theta = gradient (theta, X[j,:].reshape(1, X.shape[1]), Y[j,:].reshape(1, 1))
      theta = theta - learning_rate * d_theta
    
    cost[i] = loss(theta, X, Y)
    if i % gap == 0 :
      print ('iteration : ', i, ' loss : ', loss(theta, X, Y)) 
  return theta, cost

"""### Train Model"""

theta, cost = gradient_descent (theta, X, Y, learning_rate, max_iteration, 100)

s_theta, s_cost = stochastic_gradient_descent (s_theta, X, Y, s_learning_rate, s_max_iteration, 100)

mb_theta, mb_cost = minibatch_gradient_descent (mb_theta, X, Y, mb_learning_rate, mb_max_iteration, batch_size, 100)

"""### Optimal values of Parameters using Trained Model"""

theta

s_theta

mb_theta

"""### Cost vs Iteration Plots"""

#plot the cost
fig, ax = plt.subplots()  
ax.plot(np.arange(max_iteration), cost, 'r')  
ax.plot(np.arange(max_iteration), s_cost, 'b')  
ax.plot(np.arange(max_iteration), mb_cost, 'g')  
ax.legend(loc='upper right', labels=['batch gradient descent', 'stochastic gradient descent', 'mini-batch gradient descent'])
ax.set_xlabel('Iterations')  
ax.set_ylabel('Cost')  
ax.set_title('Error vs. Training Epoch')  

plt.show()

