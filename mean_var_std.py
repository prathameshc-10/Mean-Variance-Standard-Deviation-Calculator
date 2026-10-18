import numpy as np


def calculate(numbers):
    """Calculate statistics for a 3x3 matrix.

    Args:
        numbers: A list containing exactly nine numbers.

    Returns:
        A dictionary containing mean, variance, standard deviation,
        max, min, and sum for columns, rows, and the flattened matrix.
    """
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(numbers).reshape(3, 3)

    return {
        "mean": [
            np.mean(matrix, axis=0).tolist(),
            np.mean(matrix, axis=1).tolist(),
            np.mean(matrix).item(),
        ],
        "variance": [
            np.var(matrix, axis=0).tolist(),
            np.var(matrix, axis=1).tolist(),
            np.var(matrix).item(),
        ],
        "standard deviation": [
            np.std(matrix, axis=0).tolist(),
            np.std(matrix, axis=1).tolist(),
            np.std(matrix).item(),
        ],
        "max": [
            np.max(matrix, axis=0).tolist(),
            np.max(matrix, axis=1).tolist(),
            np.max(matrix).item(),
        ],
        "min": [
            np.min(matrix, axis=0).tolist(),
            np.min(matrix, axis=1).tolist(),
            np.min(matrix).item(),
        ],
        "sum": [
            np.sum(matrix, axis=0).tolist(),
            np.sum(matrix, axis=1).tolist(),
            np.sum(matrix).item(),
        ],
    }
