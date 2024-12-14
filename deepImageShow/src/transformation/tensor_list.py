import numpy as np
from typing import List 

def tensor_to_list(tensor: np.ndarray, col: int = 1, row: int = 1) -> List[np.ndarray]:
    """
    Convert tensor to list of images based on specified column and row dimensions.

    Args:
        tensor: Input NumPy array
        col: Number of columns to split
        row: Number of rows to split

    Returns:
        List of NumPy arrays
    """
    dimensions = tensor.shape
    col = dimensions[1] if col > 1 else 1
    row = dimensions[0] if row > 1 else 1
    tensor_list = []

    for i in range(row):
        if col == 1:
            tensor_list.append(tensor[i, :, :, :])
        else:
            for j in range(col):
                tensor_list.append(tensor[i, j, :, :])

    return tensor_list