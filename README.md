# W17D4 Demo Code - Multi-Modal AI Systems

This repository contains working code examples demonstrated during W17D4 class session on Multi-Modal AI Systems.

## Quick Start

### 1. Clone and Setup

#### Clone repository

```bash
git clone https://github.com/Justice-Through-Code/AISE26_w17_d4.git
cd AISE26_w17_d4/aise26-w17d4-demos
```

#### Create virtual environment

**Mac/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (Command Prompt):**

```cmd
python -m venv venv
venv\Scripts\activate
```

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

> **Note:** On Windows PowerShell, you may need to run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` if you encounter execution policy errors.

#### Install dependencies

```bash
pip install -r requirements.txt
```

**Note:** This installs all dependencies including audio libraries (librosa, soundfile) needed for the Whisper demo.

#### Download sample images (or use your own)

```bash
python demos/utils.py --download-samples
```

### 2. Run Demos

**Demo 1: CLIP Text-to-Image Retrieval**

```bash
python demos/01_clip_retrieval.py
```

**Demo 2: Image Captioning with BLIP**

```bash
python demos/02_image_captioning.py
```

**Demo 3: Whisper Audio Transcription (Optional)**

```bash
python demos/03_whisper_transcription.py
```

To see setup instructions for audio files:

```bash
python demos/03_whisper_transcription.py --setup-info
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

### Demo 3: Whisper Audio Transcription (Optional)

**File:** `demos/03_whisper_transcription.py`

**What it does:**

- Loads OpenAI's Whisper model for automatic speech recognition
- Transcribes audio files (.wav, .mp3) to text
- Analyzes audio quality and provides confidence estimates
- Demonstrates stress testing with various audio conditions

**Example Usage:**

```python
from demos.whisper_transcription import AudioTranscriber

transcriber = AudioTranscriber(model_name="openai/whisper-tiny")
result = transcriber.transcribe_audio("data/audio/clear_speech.wav")
print(f"Transcription: {result['text']}")
```

**Key Teaching Points:**

- Whisper handles multiple languages and accents out-of-the-box
- Background noise significantly degrades transcription quality
- Very short clips (< 2 seconds) may lack sufficient context
- Audio stress testing is critical (noise, accents, overlapping speakers)
- Fallback behavior needed for low-confidence transcriptions

**Stress Test Checklist:**

- ☐ Background noise (traffic, music, crowd)
- ☐ Various accents and dialects
- ☐ Overlapping speakers
- ☐ Very short clips (< 2 seconds)
- ☐ Low volume / quiet speech
- ☐ Fast speech

**Setting up audio files:**

Run with `--setup-info` flag to see detailed instructions for creating sample audio files:

```bash
python demos/03_whisper_transcription.py --setup-info
```

**Suggested test files:**

- `clear_speech.wav` - Clean recording in quiet environment
- `noisy_speech.wav` - Recording with background noise
- `accent_speech.wav` - Different accent or non-native speaker
- `short_clip.wav` - Very short clip (< 2 seconds)

## Repository Structure

```
aise26-w17d4-demos/
├── README.md                       # This file
├── requirements.txt                # Python dependencies
├── data/
│   ├── images/                     # Sample images for testing
│   └── audio/                      # Sample audio files for Whisper demo
├── demos/
│   ├── 01_clip_retrieval.py       # CLIP text-to-image retrieval
│   ├── 02_image_captioning.py     # BLIP image captioning
│   ├── 03_whisper_transcription.py # Whisper audio transcription (optional)
│   └── utils.py                   # Shared utility functions
└── outputs/                        # Generated outputs (created at runtime)
```

## Dependencies

**All dependencies are included in `requirements.txt` and install with one command:**
```bash
pip install -r requirements.txt
```

### Core Requirements:

```
transformers>=4.36.0
torch>=2.1.0
pillow>=10.0.0
numpy>=1.24.0
```

### Audio Libraries (for Whisper demo):

```
librosa>=0.10.0
soundfile>=0.12.0
```

### Development Tools (optional):

```
jupyter>=1.0.0
matplotlib>=3.7.0
```

## Learning Objectives

Each demo maps to specific learning objectives:

| Demo                | Learning Objective                                            |
| ------------------- | ------------------------------------------------------------- |
| CLIP Retrieval      | Explain dual encoders and shared embedding space              |
| CLIP Retrieval      | Understand similarity scoring and top-k retrieval             |
| BLIP Captioning     | Contrast retrieval (safer) vs generation (hallucination risk) |
| Whisper ASR         | Understand audio modality stress testing (noise, accents)     |
| Whisper ASR         | Implement multimodal evaluation with slice-based testing      |
| All Demos           | Use Transformers pipelines for reproducible inference         |

## Next Steps for Students

After running these demos, you should:

1. Modify queries/images to test edge cases
2. Use this code as a starting point for your assignment
3. Add stress testing (blur, low-light) to your own implementations
4. Experiment with different models and parameters

## Troubleshooting

### Model download slow?

- Models will download automatically on first run
- CLIP: ~600 MB, BLIP: ~1 GB
- Pre-download before class if possible

### GPU not detected?

- Demos work fine on CPU (just slower)
- Expect 2-5 seconds per image on CPU

### Import errors?

- Run `pip install -r requirements.txt` again
- Make sure you're in the virtual environment
- You should see `(venv)` in your terminal/command prompt

### Virtual environment activation issues (Windows PowerShell)?

If you get an error about execution policies:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Audio demo not working?

- Make sure you've installed all dependencies: `pip install -r requirements.txt` (includes audio libraries)
- If you already ran requirements.txt but get import errors, try: `pip install --upgrade librosa soundfile`
- Whisper model (tiny) is ~39 MB and downloads on first run
- If you don't have audio files, run with `--setup-info` flag for instructions
- Supported formats: .wav, .mp3, .flac, .m4a

## Platform-Specific Notes

### Mac

- Use `python3` instead of `python` if you have multiple Python versions
- You may need to install Xcode Command Line Tools: `xcode-select --install`

### Linux

- Ubuntu/Debian: You may need to install `python3-venv` first:

```bash
  sudo apt-get install python3-venv
```

- Some distributions may require `python3-pip`:

```bash
  sudo apt-get install python3-pip
```

### Windows

- Use Command Prompt or PowerShell (not Git Bash for activation)
- If using Anaconda, you can skip virtual environment creation and use conda directly

## References

- CLIP Paper: https://arxiv.org/abs/2103.00020
- BLIP Paper: https://arxiv.org/abs/2201.12086
- Whisper Paper: https://arxiv.org/abs/2212.04356
- Hugging Face Transformers Docs: https://huggingface.co/docs/transformers/
- Whisper Model Doc: https://huggingface.co/docs/transformers/en/model_doc/whisper

## License

MIT License - Feel free to use for educational purposes.
