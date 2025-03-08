# 🎨 Automatic Object Cropping Tool

A Python-based image cropping tool that automatically extracts objects from images using **YOLO**, **Pascal VOC**, and **COCO** annotation formats. The tool supports both command-line execution and an **interactive Streamlit GUI**, making it easy for managers and non-technical users to visualize and verify image annotations.

---

## 🚀 Features

- **Supports Multiple Annotation Formats**:
  - YOLO (`.txt`)
  - Pascal VOC (`.xml`)
  - COCO (`.json`)
- **Automatic Format Detection**: Automatically detects the annotation format in the selected folder.
- **Batch Processing**: Processes multiple images and annotations in one go.
- **Streamlit GUI**: User-friendly interface for uploading files, processing images, and downloading results.
- **Flexible Input Options**:
  - Upload images and annotations as **individual files**.
  - For a large number of files, upload them as a **ZIP file** (recommended).
- **Output as ZIP**: Cropped images are bundled into a downloadable ZIP file for easy sharing and access.
- **OpenCV-Powered**: Uses `opencv-python-headless` for efficient image processing.

---

## 🛠️ Installation

### 🔹 Prerequisites
- Python 3.8 or higher
- Streamlit
- OpenCV (`opencv-python-headless`)
- Other dependencies listed in `requirements.txt`

### 🔹 Clone the Repository
```bash
git clone https://github.com/Janarthanan-Radhakrishnan/automatic-object-cropping-tool.git
cd automatic-object-cropping-tool



## 📚 Important Instructions

### ✅ File Naming Convention
- **Image and annotation file names must match**.
  - Example:
    - Image: `image_01.jpg`
    - YOLO annotation: `image_01.txt`
    - Pascal VOC annotation: `image_01.xml`
    - COCO annotation: `image_01.json`
  - If file names do not match, the script will not process the image.

### ✅ Upload Options
- **Individual Files**: Upload images and annotation files directly.
- **ZIP File**: For a large number of files, zip them together and upload the ZIP file.
  - Ensure the structure inside the ZIP is flat (no nested folders).
  - All images and annotation files should be in the same directory within the ZIP.

### ✅ Output
- Cropped images are bundled into a **ZIP file** for download.
- The ZIP file contains all cropped images in a flat structure.

---

## 📘 Supported Annotation Formats

| Format      | Description                                                                 | Expected File |
|-------------|-----------------------------------------------------------------------------|---------------|
| **YOLO**    | Uses normalized coordinates (`x_center`, `y_center`, `width`, `height`)     | `.txt` file   |
| **Pascal VOC** | Uses XML files with absolute pixel values                                | `.xml` file   |
| **COCO**    | Uses JSON format with `bbox` field                                          | `.json` file  |

---

## 🤝 Contributions & Suggestions Welcome!

- **Ideas for Improvement**: If you have ideas to improve the tool, feel free to open an issue or submit a pull request.
- **Bug Reports**: If you find any bugs or edge cases, I’d love to hear your feedback.
- **Efficiency Tips**: Have a new approach or advice on making the cropping process more efficient? Let's discuss it!

Your suggestions and contributions are highly appreciated!

---

## 📬 Contact

- 📩 Email: [janasimple28@gmail.com](mailto:janasimple28@gmail.com)
- 🌐 GitHub: [Janarthanan-Radhakrishnan](https://github.com/Janarthanan-Radhakrishnan)
