# W17D4 - Breakout Session 2: Slice-Based Test Plan

## ⏱️ Time: 20 minutes (8:05 - 8:25 PM)

## 👥 Team Formation
- **Team Size:** Same teams from Breakout 1
- **Roles:** Rotate if you didn't switch in Breakout 1

---

## 🎯 Objective

Create a comprehensive, slice-based test plan for your multimodal pipeline. This mirrors W17D2's approach but applied to multimodal inputs. Your test plan must include:
1. **Vision stress slices** (blur, low light, clutter, small text, occlusion)
2. **Uncertain/refuse cases** where the system should gracefully decline
3. **Evidence table** logging actual test results
4. **Fallback UX text** (exact user-facing wording)

---

## 📦 Deliverable

**File:** `TEST_PLAN.md`

**Submission:** Paste your completed markdown into the Zoom chat when breakout rooms close.

---

## 📋 Requirements Checklist

Your test plan must include:
- [ ] **Minimum 10 test cases total**
- [ ] **4 vision stress cases** (choose from: blur, low light, clutter, small text, occlusion)
- [ ] **2 uncertain/refuse cases** (system should ask for clarity or refuse to answer)
- [ ] **4+ normal baseline cases** (to verify basic functionality)
- [ ] **Evidence table** with all 6 required columns
- [ ] **Fallback UX text** (exact wording shown to users)

---

## 🔄 Step-by-Step Instructions

### Step 1: Review Vision Stress Slice Categories (2 minutes)

Recall the **5 standard vision stress categories**:

| Category | Description | Example |
|----------|-------------|---------|
| **Blur** | Motion blur or out-of-focus | Dog running (motion blur), portrait (soft focus) |
| **Low Light** | Dark, underexposed, nighttime | Indoor scene with dim lighting, nighttime street |
| **Clutter** | Busy backgrounds, many objects | Crowded market, messy desk with 10+ objects |
| **Small Text** | OCR challenges, distant signs | Street sign 100m away, fine print on product |
| **Occlusion** | Partially hidden objects | Person half behind tree, car 70% blocked by fence |

**Your Task:** Pick **4 of 5** categories and create test cases for each.

---

### Step 2: Define Test Cases (12 minutes)

#### **A. Normal Baseline Cases (4 cases)**

These verify your pipeline works under ideal conditions.

**Examples for CLIP Retrieval:**
- `normal_01`: Query "golden retriever" with clear, well-lit dog image → Top-1 is correct
- `normal_02`: Query "red car" with sharp car photo → Top-1 is correct
- `normal_03`: Query "forest landscape" with high-res nature photo → Top-1 is correct
- `normal_04`: Query "person smiling" with clear portrait → Top-1 is correct

#### **B. Vision Stress Cases (4 cases)**

Pick 4 from the 5 categories above. Be specific about the stress factor.

**Examples:**
- `vision_blur_01`: Motion-blurred image of dog running (shutter speed too slow)
- `vision_lowlight_01`: Dark indoor cat photo (ISO 6400, noisy)
- `vision_clutter_01`: Busy farmers market with 15+ people, produce stands, signs
- `vision_smalltext_01`: Stop sign photographed from 50 meters away

#### **C. Uncertain / Refuse Cases (2 cases)**

These test whether your system gracefully handles ambiguity or inputs it should reject.

**Examples:**
- `uncertain_01`: Ambiguous blob image (abstract art, no clear object) → System should refuse or ask for clarity
- `uncertain_02`: Query "thing" (too vague) → System should ask follow-up question
- `refuse_01`: Completely black image (sensor cap left on) → System should refuse to caption
- `refuse_02`: Audio with 80% silence → System should refuse to transcribe

---

### Step 3: Fill Out Evidence Table (4 minutes)

Use the **6-column evidence table template**:

| test_case_id | input_description | expected_behavior | actual_output | pass_fail | notes_next_step |
|--------------|-------------------|-------------------|---------------|-----------|-----------------|

**Example Rows:**

| test_case_id | input_description | expected_behavior | actual_output | pass_fail | notes_next_step |
|--------------|-------------------|-------------------|---------------|-----------|-----------------|
| normal_01 | Clear image: golden retriever in park | Top-1 is "dog" or "golden retriever" | Top-1: "dog" (0.92) | ✅ PASS | Baseline working |
| vision_blur_01 | Blurred dog (motion, shutter 1/30s) | Top-1 similarity <0.6 OR shows fallback | Top-1: "cat" (0.48) | ❌ FAIL | Blur threshold exceeded, need blur-augmented training |
| vision_lowlight_01 | Dark indoor cat (ISO 6400, noisy) | Top-1 is "cat" with confidence >0.7 | Top-1: "shadow" (0.35) | ❌ FAIL | Low-light training data needed |
| uncertain_01 | Abstract blob (no clear object) | System refuses or shows "low confidence" | Fallback: "Not sure" + top-3 | ✅ PASS | Fallback triggered correctly |

**Key Points:**
- **actual_output:** Log what the system **actually returned**, not what you hoped
- **pass_fail:** Be honest. Failures are expected and required.
- **notes_next_step:** What would you do to fix this failure?

---

### Step 4: Write Fallback UX Text (2 minutes)

Write the **exact wording** users will see when the system is uncertain.

**Requirements:**
- User-friendly (no jargon like "low cosine similarity")
- Actionable (tell user what to do next)
- Honest (don't pretend to be confident when you're not)

**Good Examples:**

```
⚠️ Low Confidence Match

We're not confident in this result. Here are the top 3 possibilities:

1. Golden Retriever (52% match)
2. Labrador (48% match)
3. Mixed Breed Dog (45% match)

💡 Try a more specific search like "golden retriever puppy" or upload a clearer image.
```

```
❌ Unable to Generate Caption

This image is too dark or blurry for us to describe accurately.

💡 Please try:
- A well-lit photo
- A sharper, less blurry image
- A closer shot of the subject
```

**Bad Examples:**

❌ "Error: Confidence threshold not met." (Too technical)
❌ "Something went wrong." (Not helpful)
❌ "Please try again." (Doesn't explain why it failed)

---

## 📝 TEST_PLAN.md Template

Copy this template and fill it in:

```markdown
# Test Plan - [Your Feature Name]

**Team Members:** [Names]

**Feature:** [CLIP Retrieval / Image Captioning / Audio Transcription]

---

## Test Case Summary

| Category | Count |
|----------|-------|
| Normal Baseline | 4 |
| Vision Stress (Blur) | [0-1] |
| Vision Stress (Low Light) | [0-1] |
| Vision Stress (Clutter) | [0-1] |
| Vision Stress (Small Text) | [0-1] |
| Vision Stress (Occlusion) | [0-1] |
| Uncertain / Refuse | 2 |
| **Total** | **10+** |

---

## Evidence Table

| test_case_id | input_description | expected_behavior | actual_output | pass_fail | notes_next_step |
|--------------|-------------------|-------------------|---------------|-----------|-----------------|
| normal_01 | [Description] | [Expected] | [Actual] | ✅/❌ | [Notes] |
| normal_02 | [Description] | [Expected] | [Actual] | ✅/❌ | [Notes] |
| normal_03 | [Description] | [Expected] | [Actual] | ✅/❌ | [Notes] |
| normal_04 | [Description] | [Expected] | [Actual] | ✅/❌ | [Notes] |
| vision_[type]_01 | [Description] | [Expected] | [Actual] | ✅/❌ | [Notes] |
| vision_[type]_02 | [Description] | [Expected] | [Actual] | ✅/❌ | [Notes] |
| vision_[type]_03 | [Description] | [Expected] | [Actual] | ✅/❌ | [Notes] |
| vision_[type]_04 | [Description] | [Expected] | [Actual] | ✅/❌ | [Notes] |
| uncertain_01 | [Description] | [Expected] | [Actual] | ✅/❌ | [Notes] |
| uncertain_02 | [Description] | [Expected] | [Actual] | ✅/❌ | [Notes] |

---

## Detailed Test Cases

### Normal Baseline Cases

#### Test Case: normal_01
- **Input:** [e.g., "Clear image of golden retriever in park, sharp focus, good lighting"]
- **Query (if applicable):** [e.g., "golden retriever"]
- **Expected Behavior:** [e.g., "Top-1 result is 'dog' or 'golden retriever' with confidence >0.8"]
- **Rationale:** [e.g., "Verify baseline functionality on ideal input"]

#### Test Case: normal_02
- **Input:** [Description]
- **Query (if applicable):** [Query]
- **Expected Behavior:** [Expected]
- **Rationale:** [Why this test matters]

#### Test Case: normal_03
- **Input:** [Description]
- **Query (if applicable):** [Query]
- **Expected Behavior:** [Expected]
- **Rationale:** [Why this test matters]

#### Test Case: normal_04
- **Input:** [Description]
- **Query (if applicable):** [Query]
- **Expected Behavior:** [Expected]
- **Rationale:** [Why this test matters]

---

### Vision Stress Cases

#### Test Case: vision_blur_01
- **Input:** [e.g., "Dog running, motion blur (shutter speed 1/30s), subject velocity ~5 m/s"]
- **Stress Factor:** Blur (motion)
- **Expected Behavior:** [e.g., "Top-1 similarity <0.6 OR fallback triggered"]
- **Why This Matters:** [e.g., "Mobile photos often have motion blur; system must handle gracefully"]

#### Test Case: vision_lowlight_01
- **Input:** [Description]
- **Stress Factor:** Low Light
- **Expected Behavior:** [Expected]
- **Why This Matters:** [Rationale]

#### Test Case: vision_clutter_01
- **Input:** [Description]
- **Stress Factor:** Clutter
- **Expected Behavior:** [Expected]
- **Why This Matters:** [Rationale]

#### Test Case: vision_smalltext_01
- **Input:** [Description]
- **Stress Factor:** Small Text / OCR
- **Expected Behavior:** [Expected]
- **Why This Matters:** [Rationale]

---

### Uncertain / Refuse Cases

#### Test Case: uncertain_01
- **Input:** [e.g., "Abstract blob image, no clear object, noisy sensor data"]
- **Expected Behavior:** [e.g., "System refuses to caption OR shows fallback with 'low confidence' message"]
- **Why This Matters:** [e.g., "Prevents confident wrong answers on ambiguous inputs"]

#### Test Case: uncertain_02
- **Input:** [Description]
- **Expected Behavior:** [Expected]
- **Why This Matters:** [Rationale]

---

## Fallback UX Text

### Trigger Condition
**When does fallback activate?**
- [e.g., "If top-1 similarity score < 0.6"]
- [e.g., "If caption confidence < 70%"]
- [e.g., "If transcription has >10% [unintelligible] markers"]

### User-Facing Message

**Exact text shown to user:**

```
[Insert exact UX text here]

Example:

⚠️ Low Confidence Match

We're not confident in this result. Here are the top 3 possibilities:

1. [Result 1] (52% match)
2. [Result 2] (48% match)  
3. [Result 3] (45% match)

💡 Try a more specific search or upload a clearer image.
```

---

## Test Execution Plan

### When to Run Tests
- [ ] After initial implementation (before considering it "done")
- [ ] After any model changes or updates
- [ ] Before deploying to production

### How to Run Tests
1. [e.g., "Load test images from `test_images/` directory"]
2. [e.g., "Run `python run_tests.py --test-plan TEST_PLAN.md`"]
3. [e.g., "Log outputs to `RESULTS.md`"]
4. [e.g., "Review failures and update LIMITATIONS.md"]

### Pass/Fail Criteria
- **Pass Threshold:** [e.g., "≥8 of 10 tests pass"]
- **Required Failures:** [e.g., "Must have ≥2 documented failures to validate test rigor"]

---

## Next Steps After Testing

- [ ] Implement tests in code
- [ ] Run all 10+ test cases
- [ ] Log results in RESULTS.md evidence table
- [ ] Categorize failures (blur, low-light, hallucination, etc.)
- [ ] Write LIMITATIONS.md based on observed failures
- [ ] Define next improvements (targeted tests, data, model changes)
```

---

## 🧭 Tips for Success

### ✅ Do This:
- Be specific about inputs (e.g., "ISO 6400, noisy" not just "dark")
- Predict realistic failures (blur, low light) not unlikely edge cases (image is upside-down)
- Write fallback UX as if you're talking to a real user
- Fill in the "notes_next_step" column with actionable fixes

### ❌ Don't Do This:
- Write vague inputs like "bad image" → **Specify what makes it bad**
- Expect 10/10 tests to pass → **Failures are required**
- Write fallback UX like "Error 404" → **Be user-friendly**
- Leave "actual_output" blank → **You must predict what will happen**

---

## 📊 What Instructor Will Look For

When reviewing your TEST_PLAN.md, the instructor will check:

1. ✅ **Coverage:** Do you have 4 vision stress cases + 2 uncertain cases?
2. ✅ **Specificity:** Are inputs described concretely (not "blurry image" but "motion blur, shutter 1/30s")?
3. ✅ **Honesty:** Did you predict realistic failures (not "everything passes")?
4. ✅ **Fallback UX:** Is it user-friendly and actionable?
5. ✅ **Evidence table:** Are all 6 columns filled with realistic predictions?

---

## ⏰ Time Check

- **0-2 min:** Review vision stress categories
- **2-8 min:** Define 4 normal + 4 vision stress cases
- **8-10 min:** Define 2 uncertain/refuse cases
- **10-16 min:** Fill out evidence table
- **16-18 min:** Write fallback UX text
- **18-20 min:** Review and paste into Zoom chat

---

## 🔍 Self-Check Before Submitting

Ask yourself:
- [ ] Do I have at least 10 test cases?
- [ ] Did I include 4 different vision stress categories?
- [ ] Did I write specific input descriptions (not vague)?
- [ ] Did I predict realistic failures (not assume everything works)?
- [ ] Is my fallback UX text something I'd actually show a user?
- [ ] Did I fill in all 6 columns of the evidence table?

---

## 🚀 Ready? Go Test!

Open your text editor, copy the template above, and start building your test plan. Remember: **failures are not weaknesses—they're the raw material for improvement.**

Good luck! 🎯
