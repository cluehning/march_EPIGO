# EPIGO
**Epigenetic Information Geometry Observatory**  
*(or: Epigenetics, built like LEGO)*

---

## 1. What is EPIGO?

**EPIGO** is a research codebase for analyzing and visualizing *structured biological signals* (e.g. epigenetic tracks) using **information-theoretic and spectral methods**, with an emphasis on **interpretability and composition**.

The name breaks down as:

- **EPI** → *Epigenetics*  
- **GO** → *Geometry / Organization*  
- **EPIGO** → studying epigenetic data as **structured objects**, not just numbers

### LEGO intuition (how to think about the project)

Think of epigenetic data like **LEGO bricks**:

- Each *track* is a LEGO brick
- Bricks have:
  - shape (structure)
  - color (signal distribution)
  - texture (spectral content)
- We don’t just stack them randomly —  
  we analyze **how much information each brick carries** and **how bricks combine**

EPIGO provides:
- tools to **measure** bricks (entropy, spectra)
- tools to **compare** bricks
- tools to **visualize** how bricks differ and interact

The goal is not just prediction, but **understanding**.

---

## 2. Project structure

    EPIGO/
    ├─ neid/                 # Core analysis package
    │  ├─ __init__.py
    │  ├─ analysis.py        # Mathematical core (entropy, spectra)
    │  ├─ io.py              # Input/output helpers
    │  ├─ tracks.py          # Track-level abstractions
    │  ├─ viz.py             # Plotting utilities
    │  └─ viz_tracks.py      # Main visualization entry point
    │
    ├─ .vscode/
    │  └─ launch.json        # VS Code run configurations
    │
    └─ README.md

⚠️ `neid/` is a **Python package**, not a folder of standalone scripts.

## Quick start

1. Open the **EPIGO** folder in VS Code
2. Press **F5**
3. Choose `Run neid.viz_tracks` or `Run neid.viz`

### Why running files directly fails

EPIGO uses **relative imports** (for example `from .analysis import ...`), which only work when code is executed **as part of a package**.

If you run a file directly, Python forgets the package context.

❌ Do **not** do this:
- `python neid/viz_tracks.py`

✅ Correct rule:
- Always run EPIGO **modules**, never individual files

Think LEGO:
- You can’t understand a single brick by pretending it’s the whole set.

---

## 3. Code overview (what lives where)

### `analysis.py`
Contains the **mathematical core** of EPIGO.

Typical responsibilities:
- Shannon entropy computation
- Spectral / frequency‑domain transforms
- Low‑level numerical operations on tracks

This file answers questions like:
> *How much information does this signal contain?*  
> *At what spatial scales is structure present?*

---

### `tracks.py`
Defines **track‑level abstractions**.

Instead of passing raw arrays everywhere, EPIGO treats tracks as objects with:
- a signal
- metadata
- shared analysis methods

This keeps analysis composable and avoids duplicated logic.

---

### `io.py`
Handles **data loading and saving**.

Responsibilities include:
- reading configuration files
- loading tracks from disk
- writing outputs and intermediate results

Keeping I/O isolated prevents analysis code from becoming cluttered.

---

### `viz.py`
Provides **visualization helpers**.

This file focuses on:
- plotting signals
- visualizing entropy and spectra
- consistent visual style across analyses

No heavy computation should live here.

---

### `viz_tracks.py`
The **main entry point** for exploration.

This module:
- loads tracks
- runs analysis (entropy, spectra)
- produces visualizations

It is designed to be run as a **module**, not as a script.

---

## 4. Mathematical overview

### 4.1 Shannon entropy

Used to quantify the **information content** of a track:

- High entropy → complex / variable signal
- Low entropy → structured / repetitive signal

This allows comparison of tracks independent of biological labels.

---

### 4.2 Spectral analysis

Tracks are also analyzed in the **frequency domain**:

- Identifies dominant spatial scales
- Separates noise from structure
- Distinguishes tracks with similar entropy but different organization

Analogy:
- Entropy = how many LEGO types
- Spectrum = how bricks are arranged

---

### 4.3 Track abstractions

Tracks are treated as objects rather than raw arrays:

- Consistent interfaces
- Composable analysis
- Shared assumptions for visualization

This keeps the math modular and explicit.

---



---
### 5. Design philosophy

EPIGO is intentionally:

- **Modular** — like LEGO bricks
- **Explicit** — math is named, not hidden
- **Exploratory** — visualization is first‑class
- **Non‑magical** — no silent global state

If something breaks, it should break **clearly and locally**.

---

### 6. TL;DR

- `neid/` is a **Python package**
- Never run files directly
- Always run modules
- In VS Code:
  - open **EPIGO/**
  - press **F5**
  - choose a launch configuration

EPIGO studies epigenetic tracks as **composable LEGO structures**.

## 9. License

MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy  
of this software and associated documentation files (the "Software"), to deal  
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in  
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN  
THE SOFTWARE.