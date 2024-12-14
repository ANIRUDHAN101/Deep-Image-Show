from typing import List, Tuple
from matplotlib import pyplot as plt
import numpy as np

def plot_images(images: List[np.ndarray], num_rows: int, num_cols: int, figsize: Tuple[int, int] = (10, 8)):
    """
    Plot multiple images in a grid.

    Args:
        images: List of NumPy arrays representing images
        num_rows: Number of rows in the grid
        num_cols: Number of columns in the grid
        figsize: Figure size in inches
    """
    fig, axes = plt.subplots(num_rows, num_cols, figsize=figsize)
    
    for i, ax in enumerate(axes.flat):
        if i < len(images):
            # Normalize image if needed
            img = images[i]
            if img.max() > 1:
                img = img / 255.0
            
            ax.imshow(img)
            ax.axis('off')

    plt.tight_layout()
    plt.show()
