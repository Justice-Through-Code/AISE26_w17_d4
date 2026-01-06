"""
BLIP Image Captioning Demo

Demonstrates:
- Loading BLIP model
- Generating captions
- Hallucination risks on low-quality images
"""

import torch
import numpy as np
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from pathlib import Path


class ImageCaptioner:
    def __init__(self, model_name="Salesforce/blip-image-captioning-base"):
        """Initialize BLIP model and processor."""
        print(f"Loading BLIP model: {model_name}")
        self.processor = BlipProcessor.from_pretrained(model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(model_name)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    def caption_image(self, image_path, max_length=50):
        """Generate caption for an image."""
        # Load image
        image = Image.open(image_path).convert('RGB')

        # Preprocess
        inputs = self.processor(images=image, return_tensors="pt").to(self.device)

        # Generate caption
        with torch.no_grad():
            outputs = self.model.generate(**inputs, max_length=max_length)

        caption = self.processor.decode(outputs[0], skip_special_tokens=True)

        return caption

    def caption_with_confidence(self, image_path):
        """Generate caption and estimate confidence based on image quality."""
        caption = self.caption_image(image_path)

        # Simple heuristic: check image brightness as proxy for quality
        image = Image.open(image_path).convert('L')  # Convert to grayscale
        brightness = np.array(image).mean()

        confidence = "High" if brightness > 50 else "Low"

        return caption, confidence


def demo_image_captioning():
    """Run interactive image captioning demo."""
    print("=" * 60)
    print("BLIP Image Captioning Demo")
    print("=" * 60)

    captioner = ImageCaptioner()

    # Test images
    test_images = [
        "data/images/dog_clear.jpg",
        "data/images/cat_lowlight.jpg",
        "data/images/market_cluttered.jpg"
    ]

    for img_path in test_images:
        if not Path(img_path).exists():
            print(f"\n⚠️  Image not found: {img_path}")
            continue

        print("\n" + "-" * 60)
        print(f"Processing: {Path(img_path).name}")

        caption, confidence = captioner.caption_with_confidence(img_path)

        print(f"Caption: \"{caption}\"")
        print(f"Confidence: {confidence}", end="")

        if confidence == "High":
            print(" ✅")
        else:
            print(" ⚠️")
            print("Warning: Caption may be unreliable for dark/low-quality images")

    print("\n" + "=" * 60)
    print("Demo complete!")
    print("\n💡 Key Takeaways:")
    print("   - BLIP generates fluent captions")
    print("   - Low-quality images may cause hallucinations")
    print("   - Always validate with ground truth captions")
    print("=" * 60)


if __name__ == "__main__":
    demo_image_captioning()
