"""
Model loading and inference wrapper for W17D4 Assignment
"""

import torch
from PIL import Image
import numpy as np


class CLIPModel:
    """
    Wrapper for CLIP model (Track A: Text-to-Image Retrieval).

    TODO: Implement CLIP model wrapper
    """

    def __init__(self, model_name="openai/clip-vit-base-patch32"):
        """
        Initialize CLIP model.

        TODO: Implement initialization
        - Load CLIPModel and CLIPProcessor from transformers
        - Set device (cuda if available, else cpu)
        - Move model to device

        Args:
            model_name (str): Hugging Face model identifier
        """
        # TODO: Implement this method
        raise NotImplementedError("TODO: Implement CLIPModel.__init__()")

    def encode_image(self, image_path):
        """
        Encode image into embedding.

        TODO: Implement image encoding
        - Load image from path
        - Preprocess with processor
        - Get image features from model
        - Normalize embedding
        - Return embedding as numpy array

        Args:
            image_path (str): Path to image file

        Returns:
            np.ndarray: Image embedding (normalized)
        """
        # TODO: Implement this method
        raise NotImplementedError("TODO: Implement encode_image()")

    def encode_text(self, text):
        """
        Encode text into embedding.

        TODO: Implement text encoding
        - Preprocess text with processor
        - Get text features from model
        - Normalize embedding
        - Return embedding as numpy array

        Args:
            text (str): Text query

        Returns:
            np.ndarray: Text embedding (normalized)
        """
        # TODO: Implement this method
        raise NotImplementedError("TODO: Implement encode_text()")

    def compute_similarity(self, text_embedding, image_embeddings):
        """
        Compute similarity between text and images.

        TODO: Implement similarity computation
        - Compute dot product between text and image embeddings
        - Return similarity scores

        Args:
            text_embedding (np.ndarray): Text embedding
            image_embeddings (np.ndarray): Image embeddings (N x D)

        Returns:
            np.ndarray: Similarity scores (N,)
        """
        # TODO: Implement this method
        raise NotImplementedError("TODO: Implement compute_similarity()")

    def fallback_check(self, similarity_scores, threshold=0.6):
        """
        Check if fallback should be triggered.

        TODO: Implement fallback logic
        - Check if top-1 score is below threshold
        - Return boolean indicating if fallback needed

        Args:
            similarity_scores (np.ndarray): Similarity scores
            threshold (float): Confidence threshold

        Returns:
            bool: True if fallback should trigger, False otherwise
        """
        # TODO: Implement this method
        raise NotImplementedError("TODO: Implement fallback_check()")


class BLIPModel:
    """
    Wrapper for BLIP model (Track B: Image Captioning).

    TODO: Implement BLIP model wrapper
    """

    def __init__(self, model_name="Salesforce/blip-image-captioning-base"):
        """
        Initialize BLIP model.

        TODO: Implement initialization
        - Load BlipProcessor and BlipForConditionalGeneration
        - Set device
        - Move model to device

        Args:
            model_name (str): Hugging Face model identifier
        """
        # TODO: Implement this method
        raise NotImplementedError("TODO: Implement BLIPModel.__init__()")

    def generate_caption(self, image_path, max_length=50):
        """
        Generate caption for image.

        TODO: Implement caption generation
        - Load image from path
        - Preprocess with processor
        - Generate caption with model
        - Decode output tokens to text
        - Return caption string

        Args:
            image_path (str): Path to image file
            max_length (int): Maximum caption length

        Returns:
            str: Generated caption
        """
        # TODO: Implement this method
        raise NotImplementedError("TODO: Implement generate_caption()")

    def estimate_confidence(self, image_path):
        """
        Estimate confidence of caption.

        TODO: Implement confidence estimation
        - Simple heuristic: check image brightness/quality
        - Or: use generation log probabilities
        - Return confidence score (0-1)

        Args:
            image_path (str): Path to image file

        Returns:
            float: Confidence score (0-1)
        """
        # TODO: Implement this method
        raise NotImplementedError("TODO: Implement estimate_confidence()")


class WhisperModel:
    """
    Wrapper for Whisper model (Track C: Audio Transcription).

    TODO: Implement Whisper model wrapper (optional)
    """

    def __init__(self, model_name="openai/whisper-base"):
        """
        Initialize Whisper model.

        Args:
            model_name (str): Hugging Face model identifier
        """
        # TODO: Implement this method
        raise NotImplementedError("TODO: Implement WhisperModel.__init__()")

    def transcribe(self, audio_path):
        """
        Transcribe audio file.

        Args:
            audio_path (str): Path to audio file

        Returns:
            str: Transcription
        """
        # TODO: Implement this method
        raise NotImplementedError("TODO: Implement transcribe()")
