# Precision Overlay Generator

A lightweight Python utility for generating transparent, CAD-style measurement overlays. Designed for engineering visuals, technical thumbnails, and video post-production where a "precision artisan" aesthetic is required.

---

## 📸 Output Examples

This script generates transparent PNGs in three technical styles:

| **Style** | **Description** | **Use Case** |
| :--- | :--- | :--- |
| **Horizontal** | `<|-- [ TEXT ] --|>` | Measuring widths (e.g., battery gaps, component size). |
| **Vertical** | Up/Down arrows with text. | Measuring heights (e.g., flame height, stack thickness). |
| **Callout** | Right-angle pointer (`->`). | Labeling specific features (e.g., "1800K CORE", "CRACK"). |

> **Note:** All outputs feature a transparent background (`alpha=0.0`), making them ready to drag-and-drop directly onto video timelines (Premiere/DaVinci) or image editors (Photoshop/Canva).

---

## 🚀 Setup & Execution

**1. Create & Activate Environment**:
```bash
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Mac/Linux)
source .venv/bin/activate
```

**2. Install Dependencies**:
```bash
pip install -r requirements.txt
```

**3. Run the Script**:
```bash
python overlay.py
```

---

## 📂 Project Structure

-   `.venv/`: Virtual environment files.
-   `overlay.py`: The main calculation and plotting script.
-   `CAD_Overlay_Callout.png`
-   `CAD_Overlay_Horizontal.png`
-   `CAD_Overlay_Vertical.png`
