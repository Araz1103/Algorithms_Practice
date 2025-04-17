"""
K-Means Clustering (Concise Implementation)
-------------------------------------------
This script implements a minimal, well-documented version of the K-Means clustering algorithm using only NumPy.

Use case:
    - Great for quick testing, coding rounds, and conceptual interviews.
    - Easy to reason through and explain each component.

Functions:
    - euclidean_distance: Computes vectorized Euclidean distances
    - k_means_clustering: Runs K-Means given initial centroids and points

Returns:
    - Final centroids as a list of tuples
"""

import numpy as np

def euclidean_distance(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Compute the Euclidean distance between each row vector in array `a` and a single point `b`.

    Parameters:
    -----------
    a : np.ndarray
        A 2D NumPy array of shape (n_samples, n_features), where each row is a data point.
    
    b : np.ndarray
        A 1D NumPy array of shape (n_features,), representing a single reference point (e.g., a centroid).

    Returns:
    --------
    np.ndarray
        A 1D array of shape (n_samples,), where each element i is the Euclidean distance
        between a[i] and the point `b`.

    How It Works:
    -------------
    Step 1: (a - b)
        Uses NumPy broadcasting to subtract the vector `b` from each row of `a`.
        - If a.shape = (n, d) and b.shape = (d,), then result = (n, d)
    
    Step 2: ** 2
        Square each element in the result to prepare for distance calculation.

    Step 3: sum(axis=1)
        Sum across columns (i.e., across each feature of the point).
        This gives us the squared Euclidean distance for each row in `a`.

        🔍 What does axis=1 mean?
            - axis=0 ⇒ operate column-wise (reduce rows)
            - axis=1 ⇒ operate row-wise (reduce columns)
            - In our case: each row is a point, so we sum feature-wise.

        Example:
            a - b = [[0, 1], [2, 3], [4, 5]]
            (a - b)**2 = [[0, 1], [4, 9], [16, 25]]
            sum(axis=1) = [1, 13, 41]

    Step 4: np.sqrt(...)
        Final Euclidean distances: sqrt of the summed squares.

    Example:
    --------
    >>> a = np.array([[1, 2], [3, 4], [5, 6]])
    >>> b = np.array([1, 1])
    >>> euclidean_distance(a, b)
    array([1.0, 3.6056, 6.4031])

    This function is useful in K-Means, k-NN, and other distance-based ML algorithms.
    """

    # Vectorized Euclidean distance:
    return np.sqrt(((a - b) ** 2).sum(axis=1))


def k_means_clustering(points, k, initial_centroids, max_iterations=100):
    """
    Perform K-Means clustering to partition the given data points into k clusters.

    Parameters:
        points (list or np.ndarray): List of data points (n_samples x n_features)
        k (int): Number of clusters (centroids)
        initial_centroids (list or np.ndarray): Initial centroids (k x n_features)
        max_iterations (int): Maximum number of iterations (default: 100)

    Returns:
        List[Tuple]: Final centroid positions rounded to 4 decimal places

    Steps:
        1. Assign each point to the nearest centroid.
        2. Recompute the centroids as the mean of the assigned points.
        3. Repeat steps 1 and 2 until convergence or max_iterations.
    """
    points = np.array(points)  # Convert points to numpy array for easier manipulation
    centroids = np.array(initial_centroids)  # Convert initial centroids to numpy array

    for iteration in range(max_iterations):  # Iterate up to max_iterations
        # 1. **Assign points to the nearest centroid** based on Euclidean distance:
        distances = np.array([euclidean_distance(points, centroid) for centroid in centroids])
        # Get the index of the closest centroid for each point (min distance)
        assignments = np.argmin(distances, axis=0)  # axis=0 means we find the min distance for each point
        
        # 2. **Recompute the centroids** based on the points assigned to them:
        new_centroids = []  # Initialize an empty list to store new centroids
        
        for i in range(k):  # Iterate over the k centroids
            # Get all points assigned to centroid i
            assigned_points = points[assignments == i]
            # Calculate new centroid: average of assigned points
            if len(assigned_points) > 0:  # If there are points assigned to centroid i
                new_centroids.append(assigned_points.mean(axis=0))  # Compute mean of assigned points
            else:
                # If no points are assigned to centroid, keep the old centroid (edge case)
                new_centroids.append(centroids[i])

        # Convert list of centroids to a numpy array
        new_centroids = np.array(new_centroids) 

        # 3. **Check for convergence**: if centroids do not change, exit the loop
        if np.all(centroids == new_centroids):  # Check if centroids have not changed
            break  # Exit loop if converged

        # Update centroids with new centroids (rounding for consistency)
        centroids = np.round(new_centroids, 4)  # Round to 4 decimal places for consistency

    # Return final centroids as a list of tuples (rounded to 4 decimals)
    return [tuple(centroid) for centroid in centroids]


# Example Dry Run with Inputs:

# Assume the following inputs for the dry run:
# points = [[1, 2], [2, 3], [3, 4], [5, 6], [6, 7]]
# initial_centroids = [[1, 1], [5, 5]]
# k = 2 (we have 2 centroids)
# assignments = [0, 1, 1, 1, 1] (points 0, 1, 2, 3, and 4 are assigned to centroids 0 and 1)

# Initialization:
# centroids = [[1, 1], [5, 5]]

# **Iteration 1**:
# 1. **Assign points to nearest centroid**:
#    - distances for each centroid:
#      - For centroid 0: distances = [sqrt((1-1)^2 + (2-1)^2), sqrt((2-1)^2 + (3-1)^2), ...] = [1.0, 2.236, 3.605, 6.403, 7.810]
#      - For centroid 1: distances = [sqrt((1-5)^2 + (2-5)^2), sqrt((2-5)^2 + (3-5)^2), ...] = [5.0, 3.162, 2.236, 0.0, 2.236]
#    - **assignments**: [0, 1, 1, 1, 1] (points assigned to centroid 0 and 1)
#    - **assigned_points for centroid 0**: [[1, 2]]
#    - **assigned_points for centroid 1**: [[2, 3], [3, 4], [5, 6], [6, 7]]

# 2. **Recompute centroids**:
#    - For centroid 0, assigned points = [[1, 2]], new centroid = mean([1, 2]) = [1.0, 2.0]
#    - For centroid 1, assigned points = [[2, 3], [3, 4], [5, 6], [6, 7]], new centroid = mean([[2, 3], [3, 4], [5, 6], [6, 7]]) = [4.0, 5.0]
#    - new_centroids = [[1.0, 2.0], [4.0, 5.0]]

# **After Convergence** (if centroids do not change in subsequent iterations):
# The final centroids will be: [[1.0, 2.0], [4.0, 5.0]].
