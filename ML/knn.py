import numpy as np

def euclidean_distance(a, b):
    """
    Compute Euclidean distance between two points.
    
    Parameters:
        a (np.ndarray): A point (n_features,)
        b (np.ndarray): Another point (n_features,)

    Returns:
        float: Euclidean distance between points a and b
    """
    # Calculate the difference between the two points
    diff = a - b
    # Square the difference element-wise, then sum the squared values
    squared_diff = diff ** 2
    sum_squared_diff = squared_diff.sum()
    # Take the square root of the sum of squared differences to get the Euclidean distance
    return np.sqrt(sum_squared_diff)


def knn_classification(train_data, train_labels, test_data, k=3):
    """
    Perform K-Nearest Neighbors classification.
    
    Parameters:
        train_data (np.ndarray): Training data (n_samples x n_features)
        train_labels (np.ndarray): Labels for the training data (n_samples,)
        test_data (np.ndarray): Data to classify (n_samples x n_features)
        k (int): Number of nearest neighbors to consider (default: 3)
    
    Returns:
        np.ndarray: Predicted labels for the test data
    """
    predictions = []  # List to store the predictions for the test points
    
    # Iterate over each point in the test data
    for test_point in test_data:
        # Compute distances from the test point to all points in the training set
        distances = np.array([euclidean_distance(test_point, train_point) for train_point in train_data])
        # distances is now a list of the distances from test_point to each point in the training set

        # Get the indices of the k nearest neighbors (smallest distances)
        nearest_neighbors = np.argsort(distances)[:k]
        # np.argsort(distances) returns the indices that would sort the array `distances` in ascending order
        # [:k] selects the indices of the first k smallest distances

        # Retrieve the labels of the k nearest neighbors
        neighbor_labels = train_labels[nearest_neighbors]
        # train_labels[nearest_neighbors] retrieves the corresponding labels for the nearest neighbors

        # Perform majority voting: get the most common label among the neighbors
        unique, counts = np.unique(neighbor_labels, return_counts=True)
        # np.unique returns the unique values and their counts in `neighbor_labels`
        majority_vote = unique[np.argmax(counts)]  # The label with the highest count is chosen

        # Append the predicted label to the predictions list
        predictions.append(majority_vote)

    return np.array(predictions)  # Convert the predictions list to a numpy array and return


# Example Dry Run with Inputs:

# Training Data (train_data) - 4 points with 2 features
train_data = np.array([[1, 2], [2, 3], [3, 3], [6, 6]])
# Corresponding labels for the training points
train_labels = np.array([0, 0, 1, 1])

# Test Data (test_data) - 2 points with 2 features to classify
test_data = np.array([[1, 1], [5, 5]])

# Run KNN Classification with k=3 (3 nearest neighbors)
k = 3
predictions = knn_classification(train_data, train_labels, test_data, k)

# Output predictions
print(f"Predictions: {predictions}")

"""
### **Detailed Dry Run:**

#### **Inputs:**

- **train_data**: `[[1, 2], [2, 3], [3, 3], [6, 6]]`  
- **train_labels**: `[0, 0, 1, 1]`  
- **test_data**: `[[1, 1], [5, 5]]`  
- **k**: `3`

---

#### **Step-by-Step Execution:**

1. **First Test Point: `[1, 1]`**

   - **Calculate Euclidean Distances** between `[1, 1]` and all training points:
     - Distance from `[1, 1]` to `[1, 2]` = `sqrt((1-1)^2 + (1-2)^2)` = `1.0`
     - Distance from `[1, 1]` to `[2, 3]` = `sqrt((1-2)^2 + (1-3)^2)` = `2.236`
     - Distance from `[1, 1]` to `[3, 3]` = `sqrt((1-3)^2 + (1-3)^2)` = `2.828`
     - Distance from `[1, 1]` to `[6, 6]` = `sqrt((1-6)^2 + (1-6)^2)` = `7.810`
   - **Distances**: `[1.0, 2.236, 2.828, 7.810]`
   
   - **Indices of 3 nearest neighbors (k=3)**: `[0, 1, 2]`
   - **Labels of the nearest neighbors**: `[0, 0, 1]`
   - **Majority Vote**: `0` (Most common label among the neighbors is 0)
   - **Predicted Label for `[1, 1]`**: `0`

2. **Second Test Point: `[5, 5]`**

   - **Calculate Euclidean Distances** between `[5, 5]` and all training points:
     - Distance from `[5, 5]` to `[1, 2]` = `sqrt((5-1)^2 + (5-2)^2)` = `5.0`
     - Distance from `[5, 5]` to `[2, 3]` = `sqrt((5-2)^2 + (5-3)^2)` = `3.605`
     - Distance from `[5, 5]` to `[3, 3]` = `sqrt((5-3)^2 + (5-3)^2)` = `2.828`
     - Distance from `[5, 5]` to `[6, 6]` = `sqrt((5-6)^2 + (5-6)^2)` = `1.414`
   - **Distances**: `[5.0, 3.605, 2.828, 1.414]`
   
   - **Indices of 3 nearest neighbors (k=3)**: `[3, 2, 1]`
   - **Labels of the nearest neighbors**: `[1, 1, 0]`
   - **Majority Vote**: `1` (Most common label among the neighbors is 1)
   - **Predicted Label for `[5, 5]`**: `1`

---

#### **Final Predictions:**

- **Predictions** for the test points `[[1, 1], [5, 5]]` are `[0, 1]`.

---

#### **Explanation of Key Steps:**

1. **Euclidean Distance Calculation**:
   For each test point, we compute the Euclidean distance to each training point using the formula:

   \[
   \text{distance}(a, b) = \sqrt{\sum_{i=1}^{n} (a_i - b_i)^2}
   \]

   In the function, the difference between corresponding elements of `a` and `b` is squared and summed to get the squared Euclidean distance, which is then square-rooted.

2. **Finding Nearest Neighbors**:
   We use `np.argsort(distances)` to get the indices that would sort the distances in ascending order. The first `k` indices are chosen, representing the `k` closest training points.

   `np.argsort` works by sorting the array and returning the indices of the sorted elements.

3. **Majority Voting**:
   We use `np.unique()` to find the unique labels of the nearest neighbors and count their occurrences. The label with the highest count is selected as the prediction for that test point.

4. **Output**:
   The function returns the predicted labels for all test points as a numpy array, which is printed out at the end.
"""
