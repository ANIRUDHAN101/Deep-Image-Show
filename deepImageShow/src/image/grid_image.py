import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Optional

def create_image_grid(
    images: List[np.ndarray], 
    num_rows: Optional[int] = None, 
    num_cols: Optional[int] = None, 
    figsize: Optional[Tuple[int, int]] = None
) -> np.ndarray:
    """
    Create a grid of images and return as a NumPy array.

    Args:
        images: List of NumPy arrays representing images
        num_rows: Number of rows in the grid (optional)
        num_cols: Number of columns in the grid (optional)
        figsize: Figure size in inches (optional)

    Returns:
        NumPy array representing the grid of images
    """
    # Automatically determine grid dimensions if not provided
    total_images = len(images)
    if num_rows is None and num_cols is None:
        # Try to create as close to a square grid as possible
        num_cols = int(np.ceil(np.sqrt(total_images)))
        num_rows = int(np.ceil(total_images / num_cols))
    elif num_rows is None:
        num_rows = int(np.ceil(total_images / num_cols))
    elif num_cols is None:
        num_cols = int(np.ceil(total_images / num_rows))

    # Determine image dimensions
    first_image = images[0]
    img_height, img_width = first_image.shape[:2]

    # Auto-calculate figsize if not provided
    if figsize is None:
        # Adjust scaling factor as needed
        scale_factor = 0.5  # Adjust this to change overall grid size
        figsize = (num_cols * img_width * scale_factor / 100, 
                   num_rows * img_height * scale_factor / 100)

    # Create figure and axes
    fig, axes = plt.subplots(num_rows, num_cols, figsize=figsize)
    
    # Flatten axes for easier iteration
    axes = axes.ravel() if total_images > 1 else np.array([axes])

    # Plot images
    for i, ax in enumerate(axes):
        if i < total_images:
            # Normalize image if needed
            img = images[i]
            if img.max() > 1:
                img = img / 255.0
            
            ax.imshow(img)
            ax.axis('off')

    # Remove extra empty subplots
    for j in range(total_images, len(axes)):
        axes[j].axis('off')

    # Adjust layout and convert to image
    plt.tight_layout()
    
    # Convert plot to image
    fig.canvas.draw()
    grid_image = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    grid_image = grid_image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    
    # Close the figure to free up memory
    plt.close(fig)

    return grid_image

# Example usage:
