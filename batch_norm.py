# Batch Normalization from Scratch (NumPy)
# ----------------------------------------
# This implementation assumes input X is of shape (batch_size, num_features)
# i.e., fully-connected layer outputs. For CNNs, axis handling needs adjustment.

import numpy as np

class BatchNorm:
    def __init__(self, num_features, momentum=0.9, epsilon=1e-5):
        """
        Initializes Batch Normalization layer.

        Args:
            num_features (int): Number of input features.
            momentum (float): Momentum for updating running mean and variance.
            epsilon (float): Small constant for numerical stability during division.

        Attributes:
            gamma (np.ndarray): Learnable scale parameter.
            beta (np.ndarray): Learnable shift parameter.
            running_mean (np.ndarray): Running average of the mean for inference.
            running_var (np.ndarray): Running average of the variance for inference.
            cache (tuple): Stores intermediate values for backward pass.
        """
        self.gamma = np.ones((1, num_features))   # Scale parameter (γ)
        self.beta = np.zeros((1, num_features))   # Shift parameter (β)

        self.epsilon = epsilon
        self.momentum = momentum

        # Running estimates for inference
        self.running_mean = np.zeros((1, num_features))
        self.running_var = np.ones((1, num_features))

        # Cache for backpropagation
        self.cache = None

    def forward(self, X, training=True):
        """
        Forward pass of batch normalization.

        Formula:
            X_norm = (X - mean) / sqrt(variance + epsilon)
            out = gamma * X_norm + beta

        Args:
            X (np.ndarray): Input of shape (batch_size, num_features)
            training (bool): Whether to use batch stats or running averages

        Returns:
            np.ndarray: Batch-normalized output
        """
        if training:
            # Step 1: Compute mean and variance for the current batch
            batch_mean = np.mean(X, axis=0, keepdims=True)
            batch_var = np.var(X, axis=0, keepdims=True)

            # Step 2: Normalize the batch
            X_norm = (X - batch_mean) / np.sqrt(batch_var + self.epsilon)

            # Step 3: Scale and shift
            out = self.gamma * X_norm + self.beta

            # Step 4: Update running mean and variance
            self.running_mean = self.momentum * self.running_mean + (1 - self.momentum) * batch_mean
            self.running_var = self.momentum * self.running_var + (1 - self.momentum) * batch_var

            # Step 5: Cache for backward pass
            self.cache = (X, X_norm, batch_mean, batch_var)

        else:
            # Use running statistics for inference
            X_norm = (X - self.running_mean) / np.sqrt(self.running_var + self.epsilon)
            out = self.gamma * X_norm + self.beta

        return out

    def backward(self, dout):
        """
        Backward pass for batch normalization.

        Args:
            dout (np.ndarray): Gradient of loss w.r.t. output, shape (batch_size, num_features)

        Returns:
            dx (np.ndarray): Gradient w.r.t. input X
            dgamma (np.ndarray): Gradient w.r.t. gamma (scale)
            dbeta (np.ndarray): Gradient w.r.t. beta (shift)
        """
        X, X_norm, mean, var = self.cache
        m = X.shape[0]
        std_inv = 1. / np.sqrt(var + self.epsilon)
        std_inv = std_inv.reshape(1, -1)  # Ensure shape compatibility

        # Gradient w.r.t. beta and gamma
        dgamma = np.sum(dout * X_norm, axis=0, keepdims=True)
        dbeta = np.sum(dout, axis=0, keepdims=True)

        # Gradient w.r.t. normalized input
        dX_norm = dout * self.gamma

        # Intermediate gradients
        dvar = np.sum(dX_norm * (X - mean) * -0.5 * std_inv**3, axis=0, keepdims=True)
        dmean = np.sum(dX_norm * -std_inv, axis=0, keepdims=True) + dvar * np.mean(-2.0 * (X - mean), axis=0, keepdims=True)

        # Final gradient w.r.t. input
        dx = dX_norm * std_inv + dvar * 2 * (X - mean) / m + dmean / m

        return dx, dgamma, dbeta


# ---------------------------
# Simple Dry Run and Usage Test
# ---------------------------
if __name__ == "__main__":
    np.random.seed(42)
    bn = BatchNorm(num_features=4)

    # Simulated training data (batch_size=3, features=4)
    X = np.random.randn(3, 4) * 10 + 5  # Input distribution is wide, with offset
    print("Input X:\n", X)

    # Forward pass (Training mode)
    out = bn.forward(X, training=True)
    print("\nForward Output (Training):\n", out)

    # Simulated upstream gradient (e.g. from next layer)
    dout = np.random.randn(3, 4)
    dx, dgamma, dbeta = bn.backward(dout)
    print("\nBackward Gradients:")
    print("dx (gradient w.r.t input):\n", dx)
    print("dgamma (gradient w.r.t gamma):\n", dgamma)
    print("dbeta (gradient w.r.t beta):\n", dbeta)

    # Inference mode (should use running mean/variance)
    out_infer = bn.forward(X, training=False)
    print("\nForward Output (Inference):\n", out_infer)

    # Dry Run Notes:
    # - We manually inspect input, forward normalized output, and gradients.
    # - Running mean/var updated only during training.
    # - Inference uses saved stats instead of recalculating.
    # - Outputs should differ slightly due to running average use.

"""
========================================
BatchNorm Interview Revision Guide
========================================

🧠 Concept:
Batch Normalization normalizes the input of each layer to reduce internal covariate shift. It speeds up training, stabilizes learning, and helps mitigate vanishing/exploding gradients.

📊 Forward Formula:
1. mean = 1/m * sum(X)
2. variance = 1/m * sum((X - mean)^2)
3. X_norm = (X - mean) / sqrt(variance + epsilon)
4. out = gamma * X_norm + beta

📘 Backward Gradients:
Given dout (∂L/∂out), compute:
- ∂L/∂gamma = sum(dout * X_norm)
- ∂L/∂beta = sum(dout)
- Chain rule to compute ∂L/∂X (dx)

🎯 Key Terms:
- gamma: Learnable scale factor
- beta: Learnable shift factor
- epsilon: Numerical stability
- momentum: For running mean/var during inference

🚨 Why BatchNorm helps with vanishing/exploding gradients:
- Keeps activations well-scaled and centered (mean≈0, std≈1)
- This helps gradients maintain consistent magnitude during backpropagation

⚙️ Where to Apply:
- Before/after activation (usually before ReLU)
- Works for FC layers (this impl), CNNs (adjust axes)

📝 Mock Questions:
1. What problem does BatchNorm solve?
   - It addresses internal covariate shift by normalizing layer inputs, leading to faster and more stable training.

2. Derive the forward pass of BatchNorm.
   - Calculate batch mean and variance, normalize the inputs, and apply scale (gamma) and shift (beta).

3. Why is epsilon used in the denominator?
   - Epsilon prevents division by zero and ensures numerical stability during normalization.

4. How do you compute gradients in the backward pass?
   - Use the chain rule to backpropagate through the normalization, scale, and shift operations to get dx, dgamma, dbeta.

5. How does BatchNorm help with vanishing gradients?
   - By keeping activations standardized, it maintains healthy gradient magnitudes during backpropagation.

6. Explain the effect of gamma and beta.
   - Gamma scales the normalized activations, and beta shifts them, allowing the network to recover representational power.

7. When should you use running mean/variance vs batch stats?
   - Use batch statistics during training, and running averages during inference for consistency and stability.

8. How would you apply BatchNorm in CNNs?
   - Normalize across (N, H, W) for each channel and apply gamma/beta per channel; adjust axes accordingly.

9. Can BatchNorm be used at inference time? Why?
   - Yes, using running mean and variance from training ensures deterministic output without batch dependence.

10. Does BatchNorm reduce the need for Dropout?
   - It provides some regularization, often reducing but not eliminating the need for Dropout depending on the task.
"""
