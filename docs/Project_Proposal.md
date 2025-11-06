# University of Virginia
## Department of Electrical and Computer Engineering

**Course:** ECE 4332 / ECE 6332 — AI Hardware Design and Implementation  
**Semester:** Fall 2025  
**Proposal Deadline:** November 5, 2025 — 11:59 PM  
**Submission:** Upload to Canvas (PDF) and to GitHub (`/docs` folder)

---

# AI Hardware Project Proposal Template

## 1. Project Title
AI AI Captain
Argie Cunanan and James Jiang

MonkAI Detector
## 2. Platform Selection
**Selected platform:** TinyML — **OpenMV H7**

**Why this platform:**
- OpenMV H7 has a built-in camera module, so we can do *visual* gestures (not just IMU).
- It supports MicroPython and lightweight TinyML-style workflows.
- It matches the course’s “TinyML” category in the Project Platforms module.

---

## 3. Problem Definition
We aim to show that a very small, decision-tree–style model (inspired by the ICML 2017 paper “Resource-efficient Machine Learning in 2 KB RAM for the Internet of Things”) can run **directly on a microcontroller with a camera** to recognize a small set of gestures.

**Target gestures (3 classes):**
1. Neutral / no hands
2. One finger up
3. Finger on mouth
4. Thumbs up

This is relevant to AI hardware because it demonstrates:
- on-device inference (edge),
- feature extraction under tight MCU constraints,
- and using a non-CNN, low-footprint model for a vision-like task.

---

## 4. Technical Objectives
1. **On-device inference:** Capture image, extract features, and classify on the OpenMV H7 without sending the image to a PC for ML.
2. **Latency:** Achieve gesture classification in ≤ 200 ms per frame at a low resolution (sufficient for a 2–5 FPS demo).
3. **Small model:** Keep the decision tree + feature code in the “few KB” range to stay in the spirit of the ICML 2017 work.
4. **Accuracy:** Reach ≥ 85% accuracy on a small, self-collected dataset of the 3 gestures in similar lighting.
5. **Output integration:** Print the predicted class over serial so a host (Mac) can show the corresponding picture/icon.

---

## 5. Methodology
1. **Hardware setup**
   - Use OpenMV H7 to capture grayscale, downsampled images.
   - Fix the camera position/distance so the gestures appear in predictable regions.

2. **Data collection**
   - Collect several labeled images for each gesture using OpenMV IDE.
   - Store examples in the repo (e.g. `/gestures/`).

3. **Feature extraction (on-board)**
   - Convert to grayscale.
   - Define a few fixed Regions of Interest: e.g. mouth/lower face, hand gestures.
   - Compute simple statistics per ROI (mean brightness, count of bright pixels).
   - This yields a small feature vector (≈ 3–6 numbers).

4. **Model design (decision tree)**
   - Train a tiny decision tree in Python (off-board) on the extracted features.
   - Export the thresholds to MicroPython as nested `if/elif` statements.
   - Run this tree on every frame on the OpenMV board.

5. **Validation & metrics**
   - Accuracy on held-out gesture images.
   - Latency per frame (using OpenMV timing functions).
   - Qualitative tests under slightly different lighting and for 2 users.

---

## 6. Expected Deliverables
- **GitHub repository** created from the GitHub Classroom link with:
  - `/docs/project_outline.md` 
  - `/src/openmv_gesture.py` (camera + feature extraction + decision tree)
  - `/src/host_display.py` (optional PC script to show pictures based on serial class)
  - `/gestures/` (sample captured images)
  - updated `README.md` (project summary, setup)
- **Working on-device demo** on OpenMV H7 for 3-class gesture recognition.
- **2–3 presentation slides** for the November 6 in-class presentation.
- **Final writeup/report** at the end of the semester.

---
## 7. Team Responsibilities

| Name           | Role                          | Responsibilities                                                                 |
|----------------|-------------------------------|----------------------------------------------------------------------------------|
| Argie Cunanan  | Team Lead / Data collection   | Create repo, organize files, capture gesture images, help test accuracy         |
| James Jiang    | Embedded / TinyML implementation | Write OpenMV script, implement feature extraction, port decision tree, measure latency |
---

## 8. Timeline and Milestones

| Week / Date          | Milestone                                  | Deliverable                                  |
|----------------------|---------------------------------------------|----------------------------------------------|
| By Nov 5, 2025       | Proposal draft completed                    | PDF on Canvas + `/docs` in GitHub            |
| Nov 6, 2025 (in class)| 2–3 minute project idea presentation       | Slides or GitHub repo page                   |
| Week 2 after approval| Collect gesture data + train tiny tree      | Sample images + Python training script       |
| Week 4               | Midterm-style progress                      | OpenMV doing capture → features → class      |
| Week 6               | Integration & testing                       | Live demo with serial output                  |
| Dec. 18, 2025        | Final submission                             | Report, demo notes, cleaned GitHub repo      |

---

## 9. Resources Required
- **Hardware:** OpenMV H7 board (with camera), USB cable.
- **Software:** OpenMV IDE, Python 3 (for training/exporting the decision tree), optional `pyserial` on host.
- **Data:** Self-collected images of the 3 gestures (no external dataset required).
- **Environment:** Simple, consistent lighting/backdrop to reduce misclassification.

---

## 10. References
1. “Resource-efficient Machine Learning in 2 KB RAM for the Internet of Things,” ICML 2017.  
2. OpenMV H7 documentation (sensor, image, `get_statistics()`, ROI handling).  
