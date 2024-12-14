import re
from typing import Tuple

def parse_transformation(transformation: str) -> Tuple[str, str, str, str]:
    """
    Parses a dimension transformation string and extracts relevant components.

    Args:
        transformation: The transformation string (e.g., "bhwc->b[c(hw)]").

    Returns:
        A tuple containing:
            - left side of the transformation
            - columns dimension
            - rows dimension
            - features dimension
    """
    pattern = r"(?P<left>[a-zA-Z]*)->(?P<right>[a-zA-Z\[\](),]*)"
    dimension = r'(.)\[(.)\['
    pattern_features = r'[a-zA-Z]*$'  # Extract features from the end

    match = re.match(pattern, transformation)
    if match:
        left = match.group("left")
        right = match.group("right")

        matches = re.search(dimension, right)
        if matches:
            row = matches.group(1)
            col = matches.group(2)
            features = re.search(pattern_features, right).group()
            return left, col, row, features
        else:
            print("Dimension pattern not found in right side.")
            return left, "", "", ""
    else:
        print("Transformation pattern not found.")
        return "", "", "", ""
