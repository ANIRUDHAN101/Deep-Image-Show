from typing import Any
from .src.utils.utils import detach_to_cpu, convert_to_numpy
from .src.image.grid_plot import plot_images
from .src.image.grid_image import create_image_grid
from .src.transformation.tensor_list import tensor_to_list
from .src.transformation.parse_transfrom import parse_transformation
from einops import rearrange

def process_tensor(tensor: Any, transformation: str = "bhwc->b[c[hw", col: int = 3, row: int = 4, tensor_type='torch'):
    """
    Process and visualize tensor across different frameworks.

    Args:
        tensor: Input tensor
        transformation: Rearrangement pattern
        col: Number of columns for visualization
        row: Number of rows for visualization
    """
    
    # Move to CPU
    tensor = detach_to_cpu(tensor, tensor_type)
    
    # Parse transformation
    left, columns, rows, features = parse_transformation(transformation)

    # Rearrange tensor
    right = ' '.join(rows + columns + features)
    left = ' '.join(left)
    rearranged_tensor = rearrange(tensor, f'{left} -> {right}')
    
    # Convert to NumPy
    numpy_tensor = convert_to_numpy(rearranged_tensor, tensor_type)
    
    # Convert to list of images
    tensor_list = tensor_to_list(numpy_tensor, col, row)
    
    # Plot images
    # plot_images(tensor_list, num_rows=row, num_cols=col)
    return create_image_grid(tensor_list, num_rows=row, num_cols=col)