"""
Main pipeline entry point for W17D4 Assignment

This is skeleton code. Students should implement the TODOs below.
"""

import argparse
from pathlib import Path


def load_model(model_name):
    """
    Load the model for your chosen track.

    TODO: Implement model loading
    - For Track A (CLIP): Load CLIPModel and CLIPProcessor
    - For Track B (BLIP): Load BlipProcessor and BlipForConditionalGeneration
    - For Track C (Whisper): Load WhisperProcessor and WhisperForConditionalGeneration

    Args:
        model_name (str): Hugging Face model identifier

    Returns:
        tuple: (model, processor)
    """
    # TODO: Implement this function
    raise NotImplementedError("TODO: Implement load_model()")


def index_images(image_dir, model, processor):
    """
    Index images and store embeddings (for CLIP retrieval).

    TODO: Implement image indexing
    - Load all images from image_dir
    - Encode each image into embeddings
    - Store embeddings in memory or file
    - Return mapping of image paths to embeddings

    Args:
        image_dir (str): Directory containing images
        model: Loaded model
        processor: Loaded processor

    Returns:
        dict: Mapping of image paths to embeddings
    """
    # TODO: Implement this function
    raise NotImplementedError("TODO: Implement index_images()")


def search(query, embeddings, model, processor, top_k=5):
    """
    Search for images matching the query (for CLIP retrieval).

    TODO: Implement search
    - Encode query text into embedding
    - Compute similarity with all image embeddings
    - Return top-k results with scores
    - Implement fallback behavior for low-confidence results

    Args:
        query (str): Text query
        embeddings (dict): Image embeddings from index_images()
        model: Loaded model
        processor: Loaded processor
        top_k (int): Number of results to return

    Returns:
        list: Top-k results as (image_path, score) tuples
    """
    # TODO: Implement this function
    raise NotImplementedError("TODO: Implement search()")


def caption_image(image_path, model, processor):
    """
    Generate caption for image (for BLIP captioning).

    TODO: Implement image captioning
    - Load image from image_path
    - Generate caption using model
    - Estimate confidence score
    - Implement fallback for low-confidence captions

    Args:
        image_path (str): Path to image file
        model: Loaded model
        processor: Loaded processor

    Returns:
        tuple: (caption, confidence_score)
    """
    # TODO: Implement this function
    raise NotImplementedError("TODO: Implement caption_image()")


def transcribe_audio(audio_path, model, processor):
    """
    Transcribe audio file (for Whisper transcription).

    TODO: Implement audio transcription
    - Load audio from audio_path
    - Transcribe using model
    - Calculate word error rate if ground truth available
    - Implement fallback for low-quality audio

    Args:
        audio_path (str): Path to audio file
        model: Loaded model
        processor: Loaded processor

    Returns:
        tuple: (transcript, confidence_score)
    """
    # TODO: Implement this function
    raise NotImplementedError("TODO: Implement transcribe_audio()")


def main():
    """
    Main entry point for the pipeline.

    TODO: Implement argument parsing and main logic
    - Parse command-line arguments (mode, query, image_dir, etc.)
    - Load model
    - Run appropriate function based on mode
    - Print results
    """
    parser = argparse.ArgumentParser(description="W17D4 Multimodal Pipeline")

    # TODO: Add arguments for your pipeline
    # Examples:
    # parser.add_argument("--mode", choices=["index", "search", "caption", "transcribe"])
    # parser.add_argument("--model", default="openai/clip-vit-base-patch32")
    # parser.add_argument("--query", type=str, help="Search query")
    # parser.add_argument("--image-dir", type=str, help="Image directory")
    # parser.add_argument("--image", type=str, help="Image path for captioning")

    args = parser.parse_args()

    # TODO: Implement main logic
    print("TODO: Implement main() function")

    # Example structure:
    # model, processor = load_model(args.model)
    # if args.mode == "index":
    #     embeddings = index_images(args.image_dir, model, processor)
    # elif args.mode == "search":
    #     results = search(args.query, embeddings, model, processor)
    # ...


if __name__ == "__main__":
    main()
