"""
Whisper Audio Transcription Demo (Optional)

Demonstrates:
- Loading Whisper model for automatic speech recognition (ASR)
- Transcribing audio files to text
- Handling different audio quality conditions (stress tests)
- Confidence estimation based on audio characteristics
"""

import sys
import io
import torch
import numpy as np
import librosa
from transformers import pipeline
from pathlib import Path

# Configure UTF-8 output for Windows emoji support
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class AudioTranscriber:
    def __init__(self, model_name="openai/whisper-tiny"):
        """
        Initialize Whisper ASR model.

        Model sizes available:
        - whisper-tiny: Fastest, ~39M parameters
        - whisper-base: ~74M parameters
        - whisper-small: ~244M parameters
        - whisper-medium: ~769M parameters (requires more memory)
        - whisper-large: ~1550M parameters (GPU recommended)
        """
        print(f"Loading Whisper model: {model_name}")
        print("(First run will download the model - this may take a few minutes)")

        self.asr = pipeline(
            "automatic-speech-recognition",
            model=model_name,
            device=0 if torch.cuda.is_available() else -1
        )
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {self.device}")

    def transcribe_audio(self, audio_path):
        """Transcribe audio file to text."""
        if not Path(audio_path).exists():
            return {"error": f"File not found: {audio_path}"}

        # Load audio with librosa (avoids need for ffmpeg)
        audio, sr = librosa.load(audio_path, sr=16000)

        # Transcribe (pass numpy array instead of file path)
        # return_timestamps=True handles audio longer than 30 seconds
        result = self.asr(audio, return_timestamps=True)

        return result

    def analyze_audio_quality(self, audio_path):
        """
        Analyze audio quality metrics as proxy for transcription confidence.

        Returns signal-to-noise estimate and duration.
        """
        try:
            # Load audio
            audio, sr = librosa.load(audio_path, sr=16000)

            # Calculate duration
            duration = len(audio) / sr

            # Estimate signal quality (simple RMS energy check)
            rms_energy = np.sqrt(np.mean(audio**2))

            # Simple heuristic for quality
            if rms_energy > 0.05:
                quality = "High"
            elif rms_energy > 0.02:
                quality = "Medium"
            else:
                quality = "Low"

            return {
                "duration": duration,
                "rms_energy": rms_energy,
                "quality": quality
            }
        except Exception as e:
            return {"error": str(e)}

    def transcribe_with_confidence(self, audio_path):
        """Transcribe audio and provide quality/confidence assessment."""
        try:
            # Get transcription
            transcription = self.transcribe_audio(audio_path)

            # Check for error in transcription
            if "error" in transcription:
                return {"error": transcription["error"]}

            # Analyze audio quality
            quality_info = self.analyze_audio_quality(audio_path)

            # Check for error in quality analysis
            if "error" in quality_info:
                return {"error": quality_info["error"]}

            return {
                "text": transcription.get("text", ""),
                "quality": quality_info.get("quality", "Unknown"),
                "duration": quality_info.get("duration", 0),
                "rms_energy": quality_info.get("rms_energy", 0)
            }
        except Exception as e:
            return {"error": str(e)}


def demo_whisper_transcription():
    """Run interactive Whisper transcription demo."""
    print("=" * 60)
    print("Whisper Audio Transcription Demo (Optional)")
    print("=" * 60)
    print()

    # Determine audio directory path (works whether run from project root or demos/ directory)
    # If run from demos/, go up one level to find data/audio
    # If run from project root, use data/audio directly
    script_dir = Path(__file__).parent  # demos/ directory
    project_root = script_dir.parent     # jtc-w17d4-demos/ directory

    # Try project root first, then current directory
    audio_dir = project_root / "data" / "audio"
    if not audio_dir.exists():
        audio_dir = Path("data/audio")  # Fallback to relative path
    if not audio_dir.exists():
        print(f"⚠️  Audio directory not found: {audio_dir.absolute()}")
        print("Please create the directory and add sample audio files for testing.")
        print()
        print("Suggested test cases:")
        print("  - clear_speech.wav (clean recording)")
        print("  - noisy_speech.wav (background noise)")
        print("  - accent_speech.wav (different accent)")
        print("  - short_clip.wav (< 2 seconds)")
        print()
        print("Run with --setup-info flag for detailed instructions:")
        print("  python demos/03_whisper_transcription.py --setup-info")
        return

    # Initialize transcriber
    transcriber = AudioTranscriber()

    # Test audio files (use audio_dir to build paths)
    test_files = [
        audio_dir / "clear_speech.wav",
        audio_dir / "noisy_speech.wav",
        audio_dir / "accent_speech.wav",
        audio_dir / "short_clip.wav"
    ]

    print("\n" + "=" * 60)
    print("Processing audio files...")
    print("=" * 60)

    results = []

    for audio_path in test_files:
        if not Path(audio_path).exists():
            print(f"\n⚠️  Audio file not found: {audio_path}")
            print(f"   Skipping...")
            continue

        print("\n" + "-" * 60)
        print(f"Processing: {Path(audio_path).name}")
        print("-" * 60)

        result = transcriber.transcribe_with_confidence(audio_path)

        # Check for errors
        if "error" in result:
            print(f"❌ Error: {result['error']}")
            print("   Skipping this file...")
            results.append((Path(audio_path).name, result))
            continue

        print(f"Duration: {result['duration']:.2f}s")
        print(f"Quality: {result['quality']}", end="")

        if result['quality'] == "High":
            print(" ✅")
        elif result['quality'] == "Medium":
            print(" ⚠️")
        else:
            print(" ❌")

        print(f"\nTranscription:\n  \"{result['text']}\"")

        # Add warnings for stress cases
        if result['quality'] == "Low":
            print("\n⚠️  Warning: Low audio quality detected")
            print("   Transcription may be unreliable")
        elif result['duration'] < 1.0:
            print("\n⚠️  Warning: Very short audio clip")
            print("   Context may be insufficient for accurate transcription")

        results.append((Path(audio_path).name, result))

    # Summary
    print("\n" + "=" * 60)
    print("Demo Complete - Summary")
    print("=" * 60)

    if results:
        print("\nProcessed files:")
        for filename, result in results:
            if "error" in result:
                print(f"  ❌ {filename}: Error - {result['error']}")
            else:
                status = "✅" if result['quality'] == "High" else ("⚠️" if result['quality'] == "Medium" else "❌")
                print(f"  {status} {filename}: {result['quality']} quality")

    print("\n💡 Key Takeaways:")
    print("   - Whisper handles multiple languages and accents")
    print("   - Background noise degrades transcription quality")
    print("   - Very short clips may lack context")
    print("   - Always test with stress cases (noise, accents, overlaps)")
    print("   - Implement fallback behavior for low-confidence results")
    print("=" * 60)

    print("\n📋 Stress Test Checklist:")
    print("   ☐ Background noise (traffic, music, crowd)")
    print("   ☐ Various accents and dialects")
    print("   ☐ Overlapping speakers")
    print("   ☐ Very short clips (< 2 seconds)")
    print("   ☐ Low volume / quiet speech")
    print("   ☐ Fast speech")
    print("=" * 60)


def create_sample_info():
    """Print instructions for creating sample audio files."""
    print("\n" + "=" * 60)
    print("How to Create Sample Audio Files")
    print("=" * 60)
    print()
    print("Audio files should be placed in:")
    print("  jtc-w17d4-demos/data/audio/")
    print()
    print("Option 1: Record your own audio")
    print("  - Use your phone or computer to record short clips")
    print("  - Save as .wav or .mp3 format")
    print("  - Place in data/audio/ directory")
    print()
    print("Option 2: Use free resources")
    print("  - Common Voice dataset: https://commonvoice.mozilla.org/")
    print("  - LibriVox: https://librivox.org/ (public domain audiobooks)")
    print()
    print("Suggested test cases:")
    print("  1. clear_speech.wav - Clean recording in quiet environment")
    print("  2. noisy_speech.wav - Recording with background noise")
    print("  3. accent_speech.wav - Different accent or non-native speaker")
    print("  4. short_clip.wav - Very short clip (< 2 seconds)")
    print("=" * 60)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Whisper ASR Demo")
    parser.add_argument(
        "--setup-info",
        action="store_true",
        help="Show instructions for creating sample audio files"
    )

    args = parser.parse_args()

    if args.setup_info:
        create_sample_info()
    else:
        demo_whisper_transcription()
