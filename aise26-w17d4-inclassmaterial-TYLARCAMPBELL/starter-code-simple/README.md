# W17D4 Assignment Starter Code

This repository contains starter code and templates for the W17D4 Multimodal AI Assignment.

## What's Included

### Templates
- `templates/PIPELINE.md.template` - Pipeline design template
- `templates/TEST_PLAN.md.template` - Test plan template
- `templates/RESULTS.md.template` - Results template
- `templates/LIMITATIONS.md.template` - Limitations template
- `templates/REPRO.md.template` - Reproduction steps template

### Skeleton Code
- `src/main.py` - Main pipeline entry point (TODO: implement)
- `src/test_runner.py` - Automated test runner (TODO: implement)
- `src/models.py` - Model wrapper classes (TODO: implement)
- `src/utils.py` - Helper functions (pre-filled)

### Data
- `data/images/` - Directory for test images (you'll add these)
- `data/audio/` - Directory for test audio (optional, Track C only)

## Getting Started

### 1. Fork This Repository

Click the "Fork" button in GitHub to create your own copy.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR-USERNAME/w17d4-assignment.git
cd w17d4-assignment
```

### 3. Set Up Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Choose Your Track

Pick ONE of the three tracks:
- **Track A:** CLIP Text-to-Image Retrieval (recommended)
- **Track B:** BLIP Image Captioning
- **Track C:** Whisper Audio Transcription (optional, advanced)

### 5. Fill Out Templates

Copy templates to the root directory and fill them in:

```bash
# Copy templates
cp templates/PIPELINE.md.template PIPELINE.md
cp templates/TEST_PLAN.md.template TEST_PLAN.md
cp templates/RESULTS.md.template RESULTS.md
cp templates/LIMITATIONS.md.template LIMITATIONS.md
cp templates/REPRO.md.template REPRO.md

# Edit each file to complete your assignment
```

### 6. Implement Code

Complete the TODOs in the skeleton code:
- `src/main.py` - Implement your pipeline
- `src/test_runner.py` - Implement test automation
- `src/models.py` - Implement model wrappers

The `src/utils.py` file has pre-filled helper functions you can use.

### 7. Collect Test Data

Add at least 10 test images to `data/images/`:
- 4 normal baseline images (clear, well-lit)
- 4 vision stress images (blur, low-light, clutter, occlusion)
- 2 uncertain images (ambiguous, abstract)

### 8. Run Tests

```bash
# Index images (for CLIP)
python src/main.py --mode index --image-dir data/images/

# Run test suite
python src/test_runner.py --test-plan TEST_PLAN.md --output RESULTS.md
```

### 9. Document Results

After running tests:
- Fill in `RESULTS.md` with actual outputs
- Write `LIMITATIONS.md` based on observed failures
- Complete `REPRO.md` with exact reproduction steps

## Assignment Deliverables

Your final repository should include:

1. **PIPELINE.md** - Pipeline design with failure thinking
2. **TEST_PLAN.md** - 10+ test cases with evidence table
3. **RESULTS.md** - Filled evidence table with actual outputs
4. **LIMITATIONS.md** - 80-120 word limitations statement
5. **REPRO.md** - Exact reproduction steps
6. **src/** - Working code for your prototype
7. **data/** - Sample test data (10+ images or audio files)
8. **README.md** - Project overview (update this file)

## Grading Criteria

See `ASSIGNMENT.md` for full grading rubric. Key points:

- **Pipeline Design (15%):** Specific models, measurable success, realistic failures
- **Test Plan (25%):** 10+ tests, vision stress cases, evidence table
- **Test Execution (30%):** Actual test runs, 8+ documented failures
- **Limitations (15%):** Evidence-driven, specific, quantitative
- **Reproducibility (10%):** Clear setup steps, code runs without errors
- **Code Quality (5%):** Clean, commented, no errors

## Tips for Success

### ✅ Do This:
- Run tests and log actual failures (not predictions)
- Find at least 8 failures (if not, tests too easy)
- Write specific, quantitative limitations
- Make your code reproducible (reviewer can run without questions)
- Write user-friendly fallback UX

### ❌ Don't Do This:
- Submit predictions as results (must actually run tests)
- Write generic limitations ("may not work in all cases")
- Assume everything works (failures are required)
- Use vague inputs ("blurry image" instead of "motion blur, shutter 1/30s")

## Repository Structure

```
w17d4-assignment/
├── README.md                    # This file
├── ASSIGNMENT.md                # Full assignment specification
├── PIPELINE.md                  # Your pipeline design (to be filled)
├── TEST_PLAN.md                 # Your test plan (to be filled)
├── RESULTS.md                   # Your test results (to be filled)
├── LIMITATIONS.md               # Your limitations statement (to be filled)
├── REPRO.md                     # Your reproduction steps (to be filled)
├── requirements.txt             # Python dependencies
├── templates/                   # Empty templates
│   ├── PIPELINE.md.template
│   ├── TEST_PLAN.md.template
│   ├── RESULTS.md.template
│   ├── LIMITATIONS.md.template
│   └── REPRO.md.template
├── src/                         # Source code
│   ├── main.py                  # Main pipeline (TODO)
│   ├── test_runner.py           # Test automation (TODO)
│   ├── models.py                # Model wrappers (TODO)
│   └── utils.py                 # Helper functions (pre-filled)
├── data/                        # Test data
│   ├── images/                  # Test images (you'll add these)
│   └── audio/                   # Test audio (optional)
└── examples/                    # Example deliverables (reference)
    └── (to be added)
```

## Getting Help

**Questions?**
- Post on Ed Discussion
- Come to office hours (see Canvas for schedule)
- Review the demo code: `jtc-w17d4-demos` repository

**Common Issues:**
- Model download slow? Models download automatically on first run (2-5 min)
- GPU not available? Code works on CPU (just slower)
- Import errors? Make sure virtual environment is activated

## References

- In-class demos: `jtc-w17d4-demos` repository
- CLIP Paper: https://arxiv.org/abs/2103.00020
- BLIP Paper: https://arxiv.org/abs/2201.12086
- Whisper Paper: https://arxiv.org/abs/2212.04356
- Hugging Face Docs: https://huggingface.co/docs/transformers/

## Submission

1. Push your completed repository to GitHub
2. Submit repository link via Canvas
3. Ensure repository is public or shared with instructor

## Academic Integrity

- You may use in-class demo code as reference
- You may discuss high-level design with classmates
- Do NOT copy-paste code from classmates
- Do NOT share your repository before deadline

Good luck!
