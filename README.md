# W17D4 Demo Code - Multi-Modal AI Systems

This repository contains working code examples demonstrated during W17D4 class session on Multi-Modal AI Systems.

## Quick Start

### 1. Clone and Setup

```bash
# Clone repository
git clone https://github.com/your-org/jtc-w17d4-demos.git
cd jtc-w17d4-demos

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download sample images (or use your own)
python demos/utils.py --download-samples
```

### 2. Run Demos

```bash
# Demo 1: CLIP Text-to-Image Retrieval
python demos/01_clip_retrieval.py

# Demo 2: Image Captioning with BLIP
python demos/02_image_captioning.py
```

## What's Included

### Demo 1: CLIP Text-to-Image Retrieval

**File:** `demos/01_clip_retrieval.py`

**What it does:**
- Loads CLIP model (ViT-B/32)
- Encodes images into embeddings
- Accepts text queries and retrieves top-k similar images
- Demonstrates similarity scoring and fallback behavior

**Example Usage:**

```python
from demos.clip_retrieval import CLIPRetriever

retriever = CLIPRetriever(model_name="openai/clip-vit-base-patch32")
retriever.index_images(image_dir="data/images/")

results = retriever.search("a dog playing in a park", top_k=5)
for img_path, score in results:
    print(f"{img_path}: {score:.3f}")
```

**Key Teaching Points:**
- CLIP enables zero-shot retrieval (no training needed)
- Similarity scores are interpretable (0-1 range)
- Blurred images have lower scores
- This is a retrieval error we can observe and fix

### Demo 2: Image Captioning with BLIP

**File:** `demos/02_image_captioning.py`

**What it does:**
- Loads BLIP image captioning model
- Generates text captions for images
- Demonstrates hallucination risk on low-quality images

**Example Usage:**

```python
from demos.image_captioning import ImageCaptioner

captioner = ImageCaptioner(model_name="Salesforce/blip-image-captioning-base")

caption = captioner.caption_image("data/images/dog_clear.jpg")
print(f"Caption: {caption}")
```

**Key Teaching Points:**
- Captions are fluent and natural-sounding
- Model can hallucinate objects not in the image
- Confidence scores help, but aren't foolproof
- Ground truth captions are essential for validation

## Repository Structure

```
jtc-w17d4-demos/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── data/
│   └── images/                        # Sample images for testing
├── demos/
│   ├── 01_clip_retrieval.py          # CLIP text-to-image retrieval
│   ├── 02_image_captioning.py        # BLIP image captioning
│   └── utils.py                       # Shared utility functions
└── outputs/                           # Generated outputs (created at runtime)
```

## Dependencies

**Core Requirements:**
```
transformers>=4.36.0
torch>=2.1.0
pillow>=10.0.0
numpy>=1.24.0
```

**Optional (for Jupyter notebooks):**
```
jupyter>=1.0.0
matplotlib>=3.7.0
```

## Learning Objectives

Each demo maps to specific learning objectives:

| Demo | Learning Objective |
|------|-------------------|
| CLIP Retrieval | Explain dual encoders and shared embedding space |
| CLIP Retrieval | Understand similarity scoring and top-k retrieval |
| BLIP Captioning | Contrast retrieval (safer) vs generation (hallucination risk) |
| All Demos | Use Transformers pipelines for reproducible inference |

## Next Steps for Students

After running these demos, you should:
1. Modify queries/images to test edge cases
2. Use this code as a starting point for your assignment
3. Add stress testing (blur, low-light) to your own implementations
4. Experiment with different models and parameters

## Troubleshooting

**Model download slow?**
- Models will download automatically on first run
- CLIP: ~600 MB, BLIP: ~1 GB
- Pre-download before class if possible

**GPU not detected?**
- Demos work fine on CPU (just slower)
- Expect 2-5 seconds per image on CPU

**Import errors?**
- Run `pip install -r requirements.txt` again
- Make sure you're in the virtual environment

## References

- CLIP Paper: https://arxiv.org/abs/2103.00020
- BLIP Paper: https://arxiv.org/abs/2201.12086
- Hugging Face Docs: https://huggingface.co/docs/transformers/

## License

MIT License - Feel free to use for educational purposes.
