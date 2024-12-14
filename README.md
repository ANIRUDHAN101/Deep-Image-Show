# Deep Image Show

## Overview

The Deep Image Show is a comprehensive library designed to simplify tensor manipulation, transformation, and visualization across different deep learning frameworks. It provides flexible tools for researchers and developers working with multi-dimensional data in machine learning and computer vision projects.

## Features

- **Multi-Framework Support**: Compatible with PyTorch, TensorFlow, and JAX
- **Dynamic Tensor Transformation**: Easily rearrange and process tensors
- **Automatic Image Grid Generation**: Convert tensors to visualizable image grids
- **Flexible Visualization Options**: Customize grid layout and image processing

## Installation
```bash
git clone https://github.com/ANIRUDHAN101/Deep-Image-Show.git
cd Deep-Image-Show
pip install .
```

### Dependencies

- NumPy
- Matplotlib
- Einops
- PyTorch (optional)
- TensorFlow (optional)
- JAX (optional)

## Quick Start

### Basic Usage

```python
from deepImageShow import process

# Process and visualize a tensor
grid_image = process.process_tensor(
    tensor=your_tensor, 
    transformation="bhwc->b[c[hw", 
    col=3, 
    row=4, 
    tensor_type='torch'
)
```

## Transformation Syntax

The transformation string follows the pattern: 
`original_dimensions -> new_dimensions`

Example: 
- `"bhwc->b[c[hw"` 
  - `b`: Batch dimension
  - `h`: Height
  - `w`: Width
  - `c`: Channels

## Supported Frameworks

- PyTorch
- TensorFlow
- JAX

## Module Details

### Utilities
- `detach_to_cpu()`: Move tensors to CPU
- `convert_to_numpy()`: Convert tensors to NumPy arrays

### Image Processing
- `tensor_to_list()`: Convert tensors to image lists
- `create_image_grid()`: Generate image grids

### Transformation
- `parse_transformation()`: Parse complex transformation patterns

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - anirudhan0ks@gmail.com

Project Link: [https://github.com/ANIRUDHAN101/Deep-Image-Show.git](https://github.com/ANIRUDHAN101/Deep-Image-Show.git)

## Acknowledgments

- NumPy
- Matplotlib
- Einops
- Deep learning framework teams