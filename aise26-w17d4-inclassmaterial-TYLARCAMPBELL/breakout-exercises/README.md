# W17D4 Assignment: Reviewable Multimodal Prototype

## 📚 Assignment Overview

**Due Date:** See Canvas
**Weight:** 15% of course grade
**Submission:** GitHub repository link via Canvas
**Estimated Time:** 8-12 hours

---

## 🎯 Learning Objectives

By completing this assignment, you will demonstrate the ability to:

1. **Prototype** a multimodal AI workflow using Transformers (CLIP, BLIP, or Whisper)
2. **Design** a slice-based test plan with vision/audio stress cases
3. **Execute** systematic testing and log actual failures
4. **Document** limitations grounded in observed failures
5. **Produce** a reviewable evidence bundle (mirroring W17D2 standards)

---

## 📦 Deliverables

Submit a **GitHub repository** containing:

1. **PIPELINE.md** - Pipeline design with failure thinking
2. **TEST_PLAN.md** - 10+ test cases with evidence table
3. **RESULTS.md** - Filled evidence table with actual outputs
4. **LIMITATIONS.md** - 80-120 word limitations statement (evidence-driven)
5. **REPRO.md** - Exact reproduction steps
6. **src/** - Runnable code for your prototype
7. **data/** - Sample test images/audio (at least 10 files for stress testing)
8. **README.md** - Overview and quick start guide

---

## 🎲 Choose Your Track

Pick **ONE** of these three tracks:

### **Track A: CLIP Text-to-Image Retrieval** ⭐ (Recommended)

**User Story:**
"As a user, I can search a collection of images using natural language queries."

**Core Requirements:**

- Load and index at least 20 images
- Accept text queries and return top-5 results
- Log similarity scores for all results
- Test on 4 vision stress categories (blur, low light, clutter, occlusion)

**Success Metric:**

- Top-1 accuracy ≥ 75% on clean images
- Graceful fallback when top-1 score < 0.6

---

### **Track B: Image Captioning for Accessibility**

**User Story:**
"As a visually impaired user, I can get text descriptions of images."

**Core Requirements:**

- Generate captions for images using BLIP or similar model
- Include confidence estimation
- Test for hallucinations on low-quality images
- Define fallback behavior for low-confidence captions

**Success Metric:**

- BLEU score ≥ 0.5 on test set with ground truth captions
- <10% hallucination rate (objects not in image)

---

### **Track C: Audio Transcription + Summary** (Optional, Advanced)

**User Story:**
"As a meeting participant, I can get transcripts and summaries of audio recordings."

**Core Requirements:**

- Transcribe speech using Whisper
- Generate 2-sentence summary of transcript
- Test on audio with noise, accents, overlapping speakers
- Define fallback for low-quality audio

**Success Metric:**

- Word Error Rate (WER) ≤ 15% on clean audio
- WER ≤ 30% on noisy audio (SNR > 10dB)

---

## 📋 Detailed Requirements

### 1. PIPELINE.md

Must include:

- [ ] Feature choice with user story
- [ ] ASCII pipeline diagram showing data flow
- [ ] Input/output formats with examples
- [ ] Specific model names (e.g., "openai/clip-vit-base-patch32")
- [ ] Embedding storage strategy
- [ ] Success criteria with metrics and thresholds
- [ ] 3 expected failure modes with root causes
- [ ] Fallback behavior with exact UX text

**Length:** 200-400 words

---

### 2. TEST_PLAN.md

Must include:

- [ ] At least 10 test cases total
- [ ] 4 vision stress cases (blur, low light, clutter, small text, OR occlusion)
  - For audio track: 4 audio stress cases (noise, accents, overlapping, short clips, OR low quality)
- [ ] 2 uncertain/refuse cases
- [ ] 4+ normal baseline cases
- [ ] Evidence table with 6 columns: `test_case_id | input_description | expected_behavior | actual_output | pass_fail | notes_next_step`
- [ ] Fallback UX text (exact user-facing wording)

**Evidence Table Example:**

| test_case_id   | input_description         | expected_behavior               | actual_output       | pass_fail | notes_next_step       |
| -------------- | ------------------------- | ------------------------------- | ------------------- | --------- | --------------------- |
| normal_01      | Clear dog image           | Top-1 is "dog"                  | Top-1: "dog" (0.92) | ✅ PASS   | Baseline OK           |
| vision_blur_01 | Motion blur (dog running) | Fallback triggers OR top-1 <0.6 | Top-1: "cat" (0.48) | ❌ FAIL   | Add blur augmentation |

---

### 3. RESULTS.md

Must include:

- [ ] **Filled** evidence table (not predictions, but actual test results)
- [ ] At least 8 documented failures (if <8, tests too easy)
- [ ] Failures categorized by type (blur, hallucination, low-light, etc.)
- [ ] Screenshots or saved outputs for representative failures
- [ ] Summary statistics: `X/10 tests passed, Y/10 failed`

**Critical:** You must actually **run** your tests. Do not submit TEST_PLAN.md predictions as RESULTS.md.

---

### 4. LIMITATIONS.md

Must include:

- [ ] 80-120 words
- [ ] Specific failure scenarios grounded in your test results
- [ ] Quantitative where possible (e.g., "fails on images <50px" not "may not work on small images")
- [ ] NO generic disclaimers ("may not work in all cases")

**Example (Good):**

```
This CLIP retrieval system fails on motion-blurred images with object motion 
>5 m/s (tested on 5 cases, 4 failed). Accuracy drops from 85% on clean images 
to 52% on low-light scenes (ISO >3200). Ambiguous queries like "animal" return 
mixed results (dogs, cats, birds) without disambiguation. The system cannot 
handle queries with typos and will return irrelevant results. Designed for 
well-lit, sharp photos with clear subjects. Not suitable for nighttime 
photography or action shots without additional training data.
```

**Example (Bad):**

```
This system may not work in all cases. Performance may vary depending on input 
quality. Users should verify results. Not guaranteed to be 100% accurate.
```

---

### 5. REPRO.md

Must include:

- [ ] Exact package versions (`transformers==4.36.0`, not just `transformers`)
- [ ] Step-by-step setup instructions
- [ ] Commands to run tests
- [ ] Expected runtime ("~5 minutes on CPU")
- [ ] Test: Can a reviewer run your code without asking you ANY questions?

**Structure:**

```markdown
# Reproduction Steps

## Environment Setup
1. Python version: 3.10.x
2. Install dependencies: `pip install -r requirements.txt`
3. Expected install time: 2-3 minutes

## Running Tests
1. Download test images: `python scripts/download_data.py`
2. Index images: `python src/index_images.py --image-dir data/images/`
3. Run test suite: `python src/run_tests.py --test-plan TEST_PLAN.md`
4. View results: `cat RESULTS.md`

## Expected Outputs
- RESULTS.md will be updated with test outputs
- Console will show: "8/10 tests passed, 2 failed"
- Runtime: ~5 minutes on CPU
```

---

### 6. Code (src/)

Must include:

- [ ] Runnable Python code (not pseudocode)
- [ ] Main script that executes your pipeline
- [ ] Test runner that loads TEST_PLAN.md and outputs RESULTS.md
- [ ] Clean, commented code (not spaghetti)
- [ ] Imports use Hugging Face Transformers (not custom model implementations)

**Suggested Structure:**

```
src/
├── main.py              # Main pipeline entry point
├── test_runner.py       # Reads TEST_PLAN.md, runs tests, writes RESULTS.md
├── models.py            # Model loading and inference
└── utils.py             # Helper functions
```

---

### 7. Data (data/)

Must include:

- [ ] At least 10 test images (for vision tracks)
  - OR at least 10 test audio files (for audio track)
- [ ] Clear labels: `blur_01.jpg`, `lowlight_01.jpg`, `normal_01.jpg`
- [ ] Mix of stress cases and normal cases
- [ ] README in data/ explaining what each file tests

**Example Data Directory:**

```
data/
├── README.md            # Describes each test file
├── images/
│   ├── normal_01.jpg    # Golden retriever, clear, well-lit
│   ├── normal_02.jpg    # Red car, sharp focus
│   ├── blur_01.jpg      # Dog running, motion blur
│   ├── blur_02.jpg      # Portrait, soft focus
│   ├── lowlight_01.jpg  # Cat, dark indoor (ISO 6400)
│   ├── lowlight_02.jpg  # Street, nighttime
│   ├── clutter_01.jpg   # Farmers market, 15+ objects
│   ├── clutter_02.jpg   # Messy desk
│   ├── occlusion_01.jpg # Person half behind tree
│   └── uncertain_01.jpg # Abstract blob (no clear object)
```

---

### 8. README.md

Must include:

- [ ] One-paragraph overview of your feature
- [ ] Quick start instructions (3-5 commands)
- [ ] Link to key deliverables (PIPELINE.md, RESULTS.md, etc.)
- [ ] Summary of findings ("8/10 tests passed, main failures: blur and low-light")

---

## 🎯 Grading Rubric (100 points total)

### 1. Pipeline Design (15 points)

| Criterion         | Points | What We're Looking For                    |
| ----------------- | ------ | ----------------------------------------- |
| Model specificity | 3      | Exact model names (not "some CLIP model") |
| Success criteria  | 3      | Concrete metrics + thresholds             |
| Failure thinking  | 3      | Realistic failures with root causes       |
| Fallback UX       | 3      | User-friendly, actionable fallback text   |
| Diagram clarity   | 3      | Pipeline flow is understandable           |

### 2. Test Plan Quality (25 points)

| Criterion      | Points | What We're Looking For                           |
| -------------- | ------ | ------------------------------------------------ |
| Coverage       | 5      | 4 vision stress + 2 uncertain + 4 normal cases   |
| Specificity    | 5      | Inputs described concretely (not "blurry image") |
| Evidence table | 10     | All 6 columns filled, realistic predictions      |
| Fallback UX    | 5      | Exact user-facing text, user-friendly            |

### 3. Test Execution & Results (30 points)

| Criterion             | Points | What We're Looking For                                 |
| --------------------- | ------ | ------------------------------------------------------ |
| Actual test runs      | 10     | Evidence you ACTUALLY ran tests (not just predictions) |
| Failure documentation | 10     | At least 8 failures, categorized by type               |
| Honesty               | 5      | Transparent about what didn't work                     |
| Analysis              | 5      | Notes explain WHY tests failed                         |

### 4. Limitations Statement (15 points)

| Criterion              | Points | What We're Looking For             |
| ---------------------- | ------ | ---------------------------------- |
| Evidence-driven        | 5      | Aligned to observed failures       |
| Specificity            | 5      | Quantitative where possible        |
| Length                 | 2      | 80-120 words                       |
| No generic disclaimers | 3      | Avoids "may not work in all cases" |

### 5. Reproducibility (10 points)

| Criterion        | Points | What We're Looking For                    |
| ---------------- | ------ | ----------------------------------------- |
| Setup clarity    | 3      | Exact package versions, clear steps       |
| Commands work    | 4      | Reviewer can run without asking questions |
| Expected outputs | 3      | States what should happen                 |

### 6. Code Quality (5 points)

| Criterion           | Points | What We're Looking For     |
| ------------------- | ------ | -------------------------- |
| Runs without errors | 3      | Code executes successfully |
| Clean & commented   | 2      | Not spaghetti code         |

---

## 🚫 Common Mistakes to Avoid

### ❌ Mistake 1: Vague Inputs

**Bad:** "Blurry image"
**Good:** "Dog running, motion blur (shutter speed 1/30s, object velocity ~5 m/s)"

### ❌ Mistake 2: Assuming Everything Passes

**Bad:** "10/10 tests passed!"
**Good:** "6/10 passed, 4 failed (2 blur, 2 low-light). Added to failure log."

### ❌ Mistake 3: Generic Limitations

**Bad:** "May not work in all cases. Performance varies."
**Good:** "Fails on blurred images with motion >5 m/s. Accuracy drops 33% in low-light (ISO >3200)."

### ❌ Mistake 4: Non-Reproducible Setup

**Bad:** "Install some libraries and run the code."
**Good:** "pip install transformers==4.36.0 torch==2.1.0"

### ❌ Mistake 5: Not Testing Stress Cases

**Bad:** Only testing on perfect, well-lit images
**Good:** Deliberately testing blur, low-light, clutter, occlusion

---

## 📚 Provided Resources

### Starter Code

- Clone: `git clone https://github.com/your-org/w17d4-starter-code.git`
- Includes: Template files, sample images, utility functions

### References

- In-class demo code: `w17d4-demo-code` repository
- Hugging Face CLIP docs: https://huggingface.co/docs/transformers/model_doc/clip
- Hugging Face BLIP docs: https://huggingface.co/docs/transformers/model_doc/blip
- Hugging Face Whisper docs: https://huggingface.co/docs/transformers/model_doc/whisper

---

## 🎯 Success Criteria

You will receive **full credit** if:

1. ✅ You ran tests and logged **actual** failures (not predictions)
2. ✅ You found at least **8 failures** (if not, tests too easy)
3. ✅ Your limitations are **specific and evidence-driven**
4. ✅ A reviewer can run your code **without asking questions**
5. ✅ Your fallback UX is **user-friendly** (not technical jargon)

---

## 🆘 Getting Help

### Office Hours

- Tuesdays 4-6 PM
- Thursdays 3-5 PM
- Or by appointment

### Common Questions

**Q: What if I can't get 8 failures?**
A: Your tests are too easy. Add harder stress cases (more blur, darker low-light, etc.).

**Q: Can I use a different model than CLIP/BLIP/Whisper?**
A: Yes, but it must be from Hugging Face Transformers and must fit one of the three tracks.

**Q: How many images do I need?**
A: Minimum 10 for testing, but more is better. Quality > quantity.

**Q: Do I need a GPU?**
A: No. All demos run fine on CPU (just slower).

---

## 📅 Timeline Suggestion

| Week             | Tasks                                                 |
| ---------------- | ----------------------------------------------------- |
| **Week 1** | Choose track, set up environment, run in-class demos  |
| **Week 2** | Write PIPELINE.md and TEST_PLAN.md, collect test data |
| **Week 3** | Implement code, run tests, fill RESULTS.md            |
| **Week 4** | Write LIMITATIONS.md, polish REPRO.md, submit         |

---

## 🎓 Academic Integrity

- ✅ You may use in-class demo code as a starting point
- ✅ You may discuss high-level design with classmates
- ❌ Do not copy-paste code from classmates
- ❌ Do not share your repository before the deadline

All submissions will be checked for plagiarism.

---

## 🚀 Submission Checklist

Before submitting, verify:

- [ ] GitHub repository is public or shared with instructor
- [ ] All 8 required files are present
- [ ] Code runs without errors (test on a fresh environment)
- [ ] RESULTS.md contains actual test outputs (not predictions)
- [ ] LIMITATIONS.md is evidence-driven (not generic)
- [ ] Submitted repository link via Canvas

---

**Questions?** Post on Ed Discussion or come to office hours.

**Good luck!** 🎯
