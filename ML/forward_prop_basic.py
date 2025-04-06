import numpy as np

def g(x): #Activation Function
    return x

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

def swish(x):
    return x * sigmoid(x)

def softmax(x):
    exps = np.exp(x - np.max(x, axis=-1, keepdims=True))  # for numerical stability
    return exps / np.sum(exps, axis=-1, keepdims=True)

x = np.array([-2, 4])
W = np.array([
    [1, -3, 5],
    [2, 4, -6]
])

# W is 2 x 3
# W11 = [1, 2]
# W12 = [-3, 4]
# W13 = [5, -6]

b = np.array([-1, 1, 2])
# b11 = -1
# b12 = 1
# b13 = 2

def dense(a_in, W, b):
    num_units = W.shape[1]
    a_out = np.zeros(num_units)

    for j in range(num_units):
        # j is jth Neuron
        w = W[:, j] #weights for the jth Neuron
        z = np.dot(w, a_in) + b[j]
        a_out[j] = relu(z) #Use activation function

    return a_out

def Sequential(x, W1, W2, W3, b1, b2, b3):
    a1 = dense(x, W1, b1)
    a2 = dense(a1, W2, b2)
    a3 = dense(a2, W3, b3)
    f_x = a3
    return f_x

print(W)
print(W.shape)
print(W[:, 2]) # Extract 3rd (2 + 1) column from all rows
print(W[1, :]) # Extract 2nd (1 + 1) row from all columns
print(W[1, 2]) #Get Value from 2nd Row and 3rd Column
print(dense(x, W, b))