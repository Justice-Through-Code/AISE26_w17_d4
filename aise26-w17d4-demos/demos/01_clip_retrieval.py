"""
CLIP Text-to-Image Retrieval Demo

Demonstrates:
- Loading CLIP model
- Encoding images into embeddings
- Computing similarity scores
- Retrieving top-k results
"""

import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import numpy as np
from pathlib import Path


class CLIPRetriever:
    def __init__(self, model_name="openai/clip-vit-base-patch32"):
        """Initialize CLIP model and processor."""
        print(f"Loading CLIP model: {model_name}")
        self.model = CLIPModel.from_pretrained(model_name)
        self.processor = CLIPProcessor.from_pretrained(model_name)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

        self.image_paths = []
        self.image_embeddings = None

    def index_images(self, image_dir):
        """Encode all images in directory and store embeddings."""
        image_dir = Path(image_dir)
        self.image_paths = list(image_dir.glob("*.jpg")) + list(image_dir.glob("*.png"))

        print(f"\nIndexing {len(self.image_paths)} images...")
        embeddings = []

        for img_path in self.image_paths:
            # Load and preprocess image
            image = Image.open(img_path)
            inputs = self.processor(images=image, return_tensors="pt").to(self.device)

            # Get image embedding
            with torch.no_grad():
                image_features = self.model.get_image_features(**inputs)
                # Normalize embedding
                image_features = image_features / image_features.norm(dim=-1, keepdim=True)

            embeddings.append(image_features.cpu().numpy())
            print(f"Indexed: {img_path.name}")

        self.image_embeddings = np.vstack(embeddings)
        print(f"\n[OK] Indexing complete. {len(self.image_paths)} images ready for search.\n")

    def search(self, query_text, top_k=5):
        """Search for images matching the text query."""
        if self.image_embeddings is None:
            raise ValueError("No images indexed. Call index_images() first.")

        # Encode query text
        inputs = self.processor(text=[query_text], return_tensors="pt", padding=True).to(self.device)

        with torch.no_grad():
            text_features = self.model.get_text_features(**inputs)
            text_features = text_features / text_features.norm(dim=-1, keepdim=True)

        text_emb = text_features.cpu().numpy()

        # Compute similarity scores (dot product)
        similarities = (text_emb @ self.image_embeddings.T).squeeze()

        # Get top-k results
        top_indices = np.argsort(similarities)[::-1][:top_k]

        results = []
        print(f'Query: "{query_text}"')
        print(f"Top {top_k} Results:")
        for rank, idx in enumerate(top_indices, 1):
            img_path = self.image_paths[idx]
            score = similarities[idx]
            results.append((str(img_path), float(score)))
            print(f"{rank}. {img_path.name:20s} - Score: {score:.3f}")

        return results


def demo_clip_retrieval():
    """Run interactive CLIP retrieval demo."""
    print("=" * 60)
    print("CLIP Text-to-Image Retrieval Demo")
    print("=" * 60)

    # Initialize retriever
    retriever = CLIPRetriever()

    # Index images
    retriever.index_images("data/images/")

    # Example queries
    queries = [
        "a dog playing in a park",
        "a cat sitting indoors",
        "a crowded marketplace",
        "blurry motion"
    ]

    for query in queries:
        print("\n" + "-" * 60)
        results = retriever.search(query, top_k=3)

        # Analyze results
        top_score = results[0][1]
        if top_score < 0.6:
            print(f"\n[WARNING] Low Confidence: Top score is {top_score:.3f}")
            print("           Consider triggering fallback UX")

    print("\n" + "=" * 60)
    print("Demo complete!")
    print("=" * 60)


if __name__ == "__main__":
    demo_clip_retrieval()
