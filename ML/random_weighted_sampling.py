import numpy as np

# Define the population and their corresponding weights
elements = np.array(['apple', 'banana', 'cherry'])
weights = np.array([0.1, 0.3, 0.6])

# Perform weighted sampling without replacement
sampled_elements = np.random.choice(elements, size=2, replace=False, p=weights)
print(sampled_elements)

# Perform weighted sampling with replacement
sampled_elements = np.random.choice(elements, size=2, p=weights)
print(sampled_elements)
