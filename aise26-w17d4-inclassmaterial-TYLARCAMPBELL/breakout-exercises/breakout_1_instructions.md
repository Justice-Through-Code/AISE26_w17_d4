# W17D4 - Breakout Session 1: Pipeline Design

## ⏱️ Time: 20 minutes (7:10 - 7:30 PM)

## 👥 Team Formation
- **Team Size:** 2-3 people
- **Roles:** 
  - 1 person: Driver (shares screen, types)
  - 1-2 people: Navigators (contribute ideas, review)
  - Rotate roles halfway through (10 min mark)

---

## 🎯 Objective

Design a multimodal AI pipeline with built-in failure thinking and fallback behavior. Your goal is to demonstrate that you understand:
1. How to choose appropriate models for multimodal tasks
2. What can go wrong in multimodal systems
3. How to define measurable success criteria
4. How to handle uncertainty gracefully

---

## 📦 Deliverable

**File:** `PIPELINE.md`

**Submission:** Paste your completed markdown into the Zoom chat when breakout rooms close.

---

## 🔄 Step-by-Step Instructions

### Step 1: Choose Your Feature (5 minutes)

Pick **one** of these three options:

#### **Option A: Text-to-Image Retrieval** ⭐ (Recommended for most teams)
- **User Story:** "As a user, I can search a collection of images using natural language queries"
- **Example:** Query "dog in park" → Returns top-5 most relevant images
- **Model:** CLIP (openai/clip-vit-base-patch32)
- **Why this option:** Measurable, testable, safer than generation

#### **Option B: Image Captioning for Accessibility**
- **User Story:** "As a visually impaired user, I can get text descriptions of images"
- **Example:** Image of dog → Generated caption "A golden retriever playing in a park"
- **Model:** BLIP (Salesforce/blip-image-captioning-base)
- **Why this option:** High impact, but requires hallucination testing

#### **Option C: Audio Transcription + Summary** (Optional, advanced)
- **User Story:** "As a meeting participant, I can get transcripts and summaries of audio recordings"
- **Example:** Audio clip → Transcript + 2-sentence summary
- **Models:** Whisper (openai/whisper-base) + text summarization model
- **Why this option:** Real-world use case, but requires two-stage pipeline

---

### Step 2: Design Your Pipeline (10 minutes)

Fill out the **PIPELINE.md template** (provided below).

**Key Questions to Answer:**
1. **Inputs:** What format? (e.g., "PIL Image object" or "text string" or "WAV audio file")
2. **Outputs:** What format? (e.g., "list of 5 image URLs with scores" or "single caption string")
3. **Models:** Exactly which models from Hugging Face?
4. **Storage:** Where are embeddings or intermediate outputs stored? (e.g., "in-memory numpy array" or "SQLite database")
5. **Success Criteria:** Be specific! (e.g., "Top-1 result is correct category 80% of time on clean images")

**Create a Pipeline Diagram:**
Use ASCII art or simple text flow. Example:

```
User Query: "dog in park"
    ↓
Text Encoder (CLIP) → text_embedding (512-D)
    ↓
Similarity Search (cosine) → top_5_image_ids
    ↓
Retrieve Images from storage → [img1.jpg, img2.jpg, ...]
    ↓
Return: List of (image_url, similarity_score)
```

---

### Step 3: Define 3 Expected Failures (3 minutes)

Think about what **will** go wrong. Examples:

**For CLIP Retrieval:**
- "Blurred images: similarity scores <0.5, no clear top-1 result"
- "Ambiguous query like 'animal': returns mix of dogs, cats, birds"
- "Query with typo 'dgo' instead of 'dog': returns irrelevant results"

**For Image Captioning:**
- "Low-light image: model hallucinates objects not present"
- "Cluttered scene: caption describes only foreground, misses context"
- "Occluded object: caption says 'I see a person' but person is 90% hidden"

**For Audio Transcription:**
- "Background noise >60dB: transcription accuracy <50%"
- "Heavy accent: misses key words, transcribes 'meeting' as 'eating'"
- "Overlapping speakers: merges two speakers into one transcript"

---

### Step 4: Define Fallback Behavior (2 minutes)

What happens when the system is **uncertain**?

**Examples of Good Fallback Behavior:**
- "If top-1 similarity score <0.6, show top-3 results with message: 'Not confident. Here are closest matches.'"
- "If caption confidence <70%, show: 'Unable to generate reliable description. Please try a clearer image.'"
- "If transcription has >10 [unintelligible] markers, show: 'Audio quality too low. Please upload clearer recording.'"

**Bad Fallback Behavior (Don't do this):**
- "Return random image from collection"
- "Generate caption anyway without warning"
- "Silently fail and return empty string"

---

## 📝 PIPELINE.md Template

Copy this template and fill it in:

```markdown
# Pipeline Design - [Your Feature Name]

**Team Members:** [Names]

---

## 1. Feature Choice

**Feature:** [Option A / Option B / Option C]

**User Story:** [One sentence describing what the user can do]

---

## 2. Pipeline Diagram

```
[Insert ASCII art or text flow diagram here]
```

---

## 3. Inputs and Outputs

**Input Format:**
- Type: [e.g., PIL.Image, text string, audio file]
- Example: [e.g., "dog in park", image.jpg, audio.wav]

**Output Format:**
- Type: [e.g., List of (image_url, score), text string, dict with keys]
- Example: [e.g., `[("img1.jpg", 0.92), ("img2.jpg", 0.85), ...]`]

---

## 4. Model(s) Used

**Primary Model:**
- Name: [e.g., openai/clip-vit-base-patch32]
- Source: Hugging Face Transformers
- Task: [e.g., image-text similarity, image captioning, ASR]

**Secondary Model (if applicable):**
- Name: [e.g., none]
- Purpose: [e.g., N/A]

---

## 5. Embedding / Output Storage

**Where are embeddings or outputs stored?**
- [e.g., "In-memory NumPy array (for prototype)", "SQLite database (for production)", "Redis cache (for fast lookup)"]

**Why this choice?**
- [1-2 sentences explaining tradeoffs]

---

## 6. Success Definition

**Metric:**
- [e.g., "Top-1 accuracy on labeled test set", "BLEU score vs. ground truth captions", "Word Error Rate (WER) on transcription"]

**Threshold:**
- [e.g., "Top-1 accuracy ≥ 80% on clean images", "BLEU ≥ 0.6 on test captions", "WER ≤ 15% on clear audio"]

**Test Set Size:**
- [e.g., "100 images with ground truth labels", "50 images with human-written captions", "20 audio clips with transcripts"]

---

## 7. Three Expected Failures

### Failure 1: [Category, e.g., "Blur"]
**Description:** [e.g., "Motion-blurred image of dog running"]
**Expected Behavior:** [e.g., "Similarity scores all <0.6, no clear top-1"]
**Root Cause:** [e.g., "CLIP trained primarily on sharp images, lacks blur augmentation"]

### Failure 2: [Category, e.g., "Ambiguity"]
**Description:** [e.g., "Query 'animal' is too broad"]
**Expected Behavior:** [e.g., "Returns mix of dogs, cats, birds with similar scores"]
**Root Cause:** [e.g., "No context to disambiguate; needs follow-up question"]

### Failure 3: [Category, e.g., "Low Light"]
**Description:** [e.g., "Dark indoor image, underexposed"]
**Expected Behavior:** [e.g., "Caption hallucinates objects like 'lamp' or 'window' not present"]
**Root Cause:** [e.g., "Model trained on well-lit images, extrapolates from dark regions"]

---

## 8. Fallback Behavior

**When does fallback trigger?**
- [e.g., "If top-1 similarity score < 0.6"]

**What happens?**
- [e.g., "Show top-3 results with message: 'Low confidence. Here are closest matches. Did you mean one of these?'"]

**User Experience (exact wording):**
```
[Insert exact UX text here, e.g.:]

"⚠️ Low Confidence Match

We're not sure which image best matches your query. Here are the top 3 possibilities:

1. [Image 1] - Score: 0.58
2. [Image 2] - Score: 0.55
3. [Image 3] - Score: 0.52

Try a more specific query, like 'golden retriever in park' instead of 'dog'."
```

---

## 9. Next Steps (After This Session)

- [ ] Implement pipeline code
- [ ] Create test set with stress cases
- [ ] Log failure examples
- [ ] Write limitations statement
```

---

## 🧭 Tips for Success

### ✅ Do This:
- Be specific about models, inputs, outputs
- Think about **realistic** failures (blur, noise, ambiguity)
- Write fallback UX text as if you're talking to a real user
- Use concrete numbers (thresholds, test set sizes)

### ❌ Don't Do This:
- Say "some model" or "a neural network" → **Specify the exact Hugging Face model**
- Say "it might fail sometimes" → **Give concrete failure scenarios**
- Say "show an error" → **Write the exact error message text**
- Assume everything will work → **Failures are required, not optional**

---

## 📊 What Instructor Will Look For

When reviewing your PIPELINE.md, the instructor will check:

1. ✅ **Model specificity:** Did you name exact models?
2. ✅ **Measurable success:** Did you define a concrete metric and threshold?
3. ✅ **Realistic failures:** Did you identify failures that will actually happen?
4. ✅ **Thoughtful fallback:** Did you write user-facing fallback text?
5. ✅ **Diagram clarity:** Can someone else understand your pipeline flow?

---

## ⏰ Time Check

- **0-5 min:** Choose feature (vote as team if needed)
- **5-15 min:** Fill out template sections 1-6
- **15-18 min:** Define 3 failures and fallback behavior
- **18-20 min:** Review, polish, paste into Zoom chat

---

## 🚀 Ready? Go Build!

Open your text editor, copy the template above, and start designing your pipeline. Remember: **failure thinking is not optional—it's the core of this exercise.**

Good luck! 🎯
