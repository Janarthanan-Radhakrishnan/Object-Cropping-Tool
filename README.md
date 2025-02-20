# 🎨 Automatic Object Cropping Tool  
A **Python-based image cropping tool** that automatically extracts objects from images using **YOLO, Pascal VOC, and COCO annotation formats**. The tool supports both **command-line execution** and an **interactive Streamlit GUI** for ease of use.  

---

## 🚀 Features  
✅ Supports **YOLO, Pascal VOC, and COCO** annotation formats  
✅ Automatically detects the annotation format in the selected folder  
✅ Uses **OpenCV** for image processing and cropping  
✅ Interactive **Streamlit** app for user-friendly operation  
✅ Batch processing of images with automatic subfolder organization  
✅ Outputs cropped images into a specified directory  

---

## 🛠️ Installation  

### 🔹 Clone the Repository  
```sh
git clone https://github.com/Janarthanan-Radhakrishnan/automatic-object-cropping-tool.git
cd automatic-object-cropping-tool
```

## 📚 Important Instructions  
✅ **Image and annotation file names must match**  
- If your image is **`image_01.jpg`**, then:  
  - YOLO annotation → `image_01.txt`  
  - Pascal VOC annotation → `image_01.xml`  
  - COCO annotation → `image_01.json`  
- If file names do not match, the script **will not process the image**.  

✅ **Ensure correct folder structure**  
- Place images and annotation files **in the same directory** before running the script.  

✅ **Output folders are auto-created**  
- Cropped images are saved inside a subfolder **with the same name as the original image (without extension)**.  

---

## 📘 Supported Annotation Formats  
| Format      | Description | Expected File |
|------------|-------------|--------------|
| **YOLO**   | Uses normalized coordinates `(x_center, y_center, width, height)` | `.txt` file |
| **Pascal VOC** | Uses XML files with absolute pixel values | `.xml` file |
| **COCO**   | Uses JSON format with `bbox` field | `.json` file |

---

## 🤝 Contributions & Suggestions Welcome!  
🔹 If you have **ideas to improve the tool**, feel free to open an **issue** or submit a **pull request**.  
🔹 If you find any **bugs or edge cases**, I’d love to hear your feedback.  
🔹 Have a **new approach or advice** on making the cropping process more efficient? Let's discuss it!  

📢 **Your suggestions & contributions are highly appreciated!**  

---

## 📬 Contact  
📩 **Email:** janasimple28@gmail.com  
💼 **LinkedIn:** [Janarthanan Radhakrishnan](https://www.linkedin.com/in/janarthanan-radhakrishnan-1765a4201)  
