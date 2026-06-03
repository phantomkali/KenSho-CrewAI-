🧠 KenSho

**Agent AI–Based System for Identifying Hidden PTSD Triggers in Dream Descriptions**


KenSho is a **modular, multi-agent artificial intelligence system** designed to analyze **dream descriptions**, extract **clinically grounded semantic meaning**, identify **latent PTSD-related triggers**, and generate **clinician-ready interpretive reports**.

The system integrates **Natural Language Processing (NLP)** with **DSM-5 and ICD-11 guidelines** to support early detection, research, and psychological assessment workflows.

---

## 📌 Problem Statement

Traditional PTSD assessment methods rely heavily on:

* Questionnaires
* Interviews
* Supervised clinical evaluation

However, **dreams often encode trauma indirectly** through symbolism, emotions, and sensory cues that are difficult to identify using conventional tools or surface-level NLP models.

**KenSho addresses this gap** by converting subjective dream narratives into **structured, interpretable, and clinically aligned outputs**.

---

## 🚀 Key Features

* 🧩 **Multi-Agent Architecture** (Semantic → Trigger → Report)
* 📄 **ICD-11–Aligned Semantic JSON Extraction**
* 🎯 **DSM-5–Mapped PTSD Trigger Detection**
* 🧠 **Latent & Symbolic Trauma Cue Identification**
* 🧾 **Clinician-Ready Markdown Reports**
* 🔍 **Explainable & Reproducible Analysis**
* 💾 **Persisted Intermediate Outputs (JSON)**

---

## 🏗️ System Architecture

### Agent Crews

| Crew Name         | Role                                             | Input                                 | Output                 |
| ----------------- | ------------------------------------------------ | ------------------------------------- | ---------------------- |
| **Semantic Crew** | Extract structured semantics aligned with ICD-11 | Dream text, Guidelines                | `semantic_result.json` |
| **Trigger Crew**  | Identify hidden PTSD triggers                    | Dream text, Semantic JSON, Guidelines | `triggers_result.json` |
| **Report Crew**   | Generate clinician-ready report                  | Semantic + Trigger JSON               | `dream_report.md`      |

---

## 🔄 Execution Flow

1. **Dream Input**

   * User submits a dream description (UI or function call)
   * Clinical guidelines loaded from `guidelines.md`

2. **Semantic Analysis**

   * Converts free-text dream into structured semantic fields:

     * `event_type`
     * `context`
     * `symptoms`
     * `specific_events`
   * Output → `output/dream_semantic.json`

3. **Trigger Detection**

   * Maps dream semantics to PTSD criteria
   * Identifies trigger categories:

     * People
     * Places
     * Emotions
     * Sensory cues
     * Situational contexts
   * Output → `output/dream_triggers.json`

4. **Report Generation**

   * Integrates all analyses into a clinician-ready markdown report:

     * Overview
     * Dream Semantics Analysis
     * PTSD Trigger Analysis
     * Cross-Analysis Insights
     * Clinical Interpretation
   * Output → `output/dream_report.md`

---

## 📘 Guidelines Integration

KenSho uses **agent-readable clinical guidelines**, including:

### DSM-5

* Criterion A–H:

  * Stressor
  * Intrusion
  * Avoidance
  * Negative Mood & Cognition
  * Arousal
  * Duration
  * Functional Impact
  * Exclusion

### ICD-11

* PTSD Core Features
* Complex PTSD Indicators

### Mapping Strategy

* Entity extraction
* Emotion and sensation detection
* Temporal & spatial cue analysis
* Symbolic trauma pattern recognition
* Weighted scoring for trigger likelihood

---

## 🧪 Output Artifacts

```text
output/
├── dream_semantic.json
├── dream_triggers.json
└── dream_report.md
```

All intermediate outputs are **persisted**, enabling:

* Auditability
* Clinical review
* Research reproducibility

---

## 🏆 Advantages Over Prior Art

* Specialized **agent-based clinical reasoning**
* Transparent intermediate representations (JSON)
* Official DSM-5 / ICD-11 grounding
* Detection of **hidden, symbolic PTSD triggers**
* Automated yet interpretable report generation
* Modular and extensible architecture

---

## 🧬 Novelty & Patentable Elements

1. Multi-agent AI workflow for dream-based PTSD analysis
2. ICD-11-aligned semantic representation of dreams
3. DSM-5-mapped trigger detection for latent trauma cues
4. Automated clinician-ready report generation
5. Structured, agent-readable psychiatric guidelines
6. Fully reproducible, stage-wise persisted analysis

## ⚠️ Disclaimer

> **KenSho is a research and decision-support system.**
> It is **not a diagnostic tool** and should **not replace professional clinical evaluation**.

---

## 📄 License

Specify license here (e.g., MIT, Apache-2.0, Research-Only).

---

## 🤝 Contributions

Role: AI / NLP Developer – PTSD Trigger Analysis & Clinical Reporting
Key Contributions: Trigger detection logic, DSM-5 mapping, markdown report generation, guideline integration
