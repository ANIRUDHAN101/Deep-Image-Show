import numpy as np
from typing import Any
 
def detach_to_cpu(tensor: Any, framework: str = 'torch') -> Any:
    """
    Move tensor to CPU across different frameworks.

    Args:
        tensor: Input tensor
        framework: Tensor framework ('torch', 'tf', or 'jax')

    Returns:
        Tensor/array on CPU
    """
    if framework == 'torch':
        return tensor.detach().cpu()
    elif framework == 'tf':
        return tensor
    elif framework == 'jax':
        return tensor
    else:
        raise ValueError("Unsupported framework")

def convert_to_numpy(tensor: Any, framework: str = 'torch') -> np.ndarray:
    """
    Convert tensor to NumPy array across different frameworks.

    Args:
        tensor: Input tensor
        framework: Tensor framework ('torch', 'tf', or 'jax')

    Returns:
        NumPy array
    """
    if framework == 'torch':
        return tensor.numpy()
    elif framework == 'tf':
        return tensor.numpy()
    elif framework == 'jax':
        return np.array(tensor)
    else:
        raise ValueError("Unsupported framework")