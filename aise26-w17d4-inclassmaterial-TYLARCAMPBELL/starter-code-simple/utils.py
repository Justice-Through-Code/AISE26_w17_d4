"""
Utility helper functions for W17D4 Assignment

These functions are pre-filled to help you get started.
"""

from PIL import Image
import numpy as np
from pathlib import Path


def load_image(image_path):
    """
    Load image from path and convert to RGB.

    Args:
        image_path (str): Path to image file

    Returns:
        PIL.Image: Image in RGB format
    """
    image = Image.open(image_path).convert('RGB')
    return image


def calculate_brightness(image_path):
    """
    Calculate mean brightness of image.

    Useful for confidence estimation in BLIP captioning.

    Args:
        image_path (str): Path to image file

    Returns:
        float: Mean brightness (0-255)
    """
    image = Image.open(image_path).convert('L')  # Convert to grayscale
    arr = np.array(image)
    return arr.mean()


def normalize_embedding(embedding):
    """
    Normalize embedding to unit length.

    Args:
        embedding (np.ndarray): Embedding vector

    Returns:
        np.ndarray: Normalized embedding
    """
    norm = np.linalg.norm(embedding)
    if norm == 0:
        return embedding
    return embedding / norm


def format_output(results, top_k=5):
    """
    Format search results for display.

    Args:
        results (list): List of (image_path, score) tuples
        top_k (int): Number of results to display

    Returns:
        str: Formatted output string
    """
    output = f"Top {top_k} Results:\n"
    for rank, (img_path, score) in enumerate(results[:top_k], 1):
        filename = Path(img_path).name
        output += f"{rank}. {filename:30s} - Score: {score:.3f}\n"
    return output


def get_image_stats(image_path):
    """
    Calculate basic statistics for an image.

    Useful for debugging and understanding test inputs.

    Args:
        image_path (str): Path to image file

    Returns:
        dict: Dictionary with image statistics
    """
    img = Image.open(image_path).convert('RGB')
    arr = np.array(img)

    return {
        "shape": arr.shape,
        "mean_brightness": arr.mean(),
        "std_brightness": arr.std(),
        "min_value": arr.min(),
        "max_value": arr.max()
    }


def create_fallback_message(top_results, threshold=0.6):
    """
    Create user-friendly fallback message for low-confidence results.

    Args:
        top_results (list): List of (image_path, score) tuples
        threshold (float): Confidence threshold

    Returns:
        str: Fallback message
    """
    message = f"⚠️ Low Confidence Match\n\n"
    message += f"We're not confident in this result (top score: {top_results[0][1]:.2f} < {threshold}).\n"
    message += f"Here are the top 3 possibilities:\n\n"

    for rank, (img_path, score) in enumerate(top_results[:3], 1):
        filename = Path(img_path).name
        percentage = int(score * 100)
        message += f"{rank}. {filename} - {percentage}% match\n"

    message += f"\n💡 Try a more specific query or upload a clearer image."

    return message


def save_embeddings(embeddings, image_paths, output_path):
    """
    Save embeddings and image paths to disk.

    Args:
        embeddings (np.ndarray): Image embeddings (N x D)
        image_paths (list): List of image paths
        output_path (str): Path to save embeddings
    """
    np.save(output_path, embeddings)
    paths_file = Path(output_path).with_suffix('.txt')
    with open(paths_file, 'w') as f:
        for path in image_paths:
            f.write(f"{path}\n")


def load_embeddings(embeddings_path):
    """
    Load embeddings and image paths from disk.

    Args:
        embeddings_path (str): Path to embeddings file

    Returns:
        tuple: (embeddings, image_paths)
    """
    embeddings = np.load(embeddings_path)
    paths_file = Path(embeddings_path).with_suffix('.txt')
    with open(paths_file, 'r') as f:
        image_paths = [line.strip() for line in f]
    return embeddings, image_paths
