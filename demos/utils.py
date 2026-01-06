"""
Utility functions for W17D4 demos
"""

import requests
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import numpy as np


def download_sample_images():
    """Download sample test images."""
    print("Downloading sample images...")

    # Create data directory
    data_dir = Path("data/images")
    data_dir.mkdir(parents=True, exist_ok=True)

    # Sample URLs (replace with actual sample images)
    samples = {
        "dog_clear.jpg": "https://example.com/dog_clear.jpg",
        "dog_blurred.jpg": "https://example.com/dog_blurred.jpg",
        "cat_lowlight.jpg": "https://example.com/cat_lowlight.jpg",
        "market_cluttered.jpg": "https://example.com/market_cluttered.jpg"
    }

    for filename, url in samples.items():
        output_path = data_dir / filename
        if output_path.exists():
            print(f"  ✓ {filename} already exists")
            continue

        print(f"  Downloading {filename}...")
        # In production, use actual image URLs
        # For demo, create placeholder
        create_placeholder_image(output_path, filename)

    print("✅ Sample images ready in data/images/")


def create_placeholder_image(path, label):
    """Create a placeholder image for testing."""
    # Create a simple colored image with text
    img = Image.new('RGB', (640, 480), color=(100, 100, 100))
    draw = ImageDraw.Draw(img)
    draw.text((50, 200), label, fill=(255, 255, 255))
    img.save(path)


def calculate_image_stats(image_path):
    """Calculate basic statistics for an image."""
    img = Image.open(image_path).convert('RGB')
    arr = np.array(img)

    return {
        "mean_brightness": arr.mean(),
        "std_brightness": arr.std(),
        "shape": arr.shape
    }


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--download-samples", action="store_true")
    args = parser.parse_args()

    if args.download_samples:
        download_sample_images()
