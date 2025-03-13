# 🚀 Object Detection with OpenCV & YOLO | Interactive UI 🎯

🔍 **Real-time Object Detection using YOLO and OpenCV** with a **scrollable, interactive UI** for selecting object categories dynamically.

---

## 📸 **Demo**
![image](https://github.com/user-attachments/assets/02782d9b-c665-4a15-8df0-e6c4fd8d4634)

---

## 🎯 **Project Overview**
This project implements **real-time object detection** using **YOLO (You Only Look Once)** and **OpenCV** in Python. It features:
✅ **Deep Learning-based Object Detection (YOLOv4-tiny)**  
✅ **Customizable Object Selection via UI Buttons**  
✅ **Scrollable Category Panel** (Supports 80+ object categories)  
✅ **Optimized UI** (Compact, modern, and business-ready)  
✅ **Fast and Efficient** (Utilizing OpenCV’s DNN module)

---

## 📂 **Project Structure**
```
opencv-object-detection-ui/
 ├── dnn_model/                  # YOLO model files
 │    ├── yolov4-tiny.cfg
 │    ├── yolov4-tiny.weights
 │    ├── classes.txt
 ├── main4.py                     # Main object detection script
 ├── gui_buttons.py                # GUI button system with scrolling support
 ├── README.md                     # Project documentation
```

---

## 🛠️ **Installation & Setup**

### 🔹 1. Clone the Repository
```bash
git clone https://github.com/Reality361/opencv-object-detection-ui.git
cd opencv-object-detection-ui
```

### 🔹 2. Install Dependencies
Ensure you have installed dependencies about OpenCV.

📌 **Dependencies include:**  
- `opencv-python`
- `numpy`

### 🔹 3. Download YOLO Weights
The project requires **YOLOv4-tiny pre-trained weights**.  
📥 Download them from: [YOLO Weights](https://github.com/AlexeyAB/darknet/releases)  
Place them inside the `dnn_model/` directory:
```
dnn_model/
 ├── yolov4-tiny.cfg
 ├── yolov4-tiny.weights
 ├── classes.txt
```

---

## ▶️ **Running the Object Detector**
```bash
python main4.py
```

📌 **Controls:**
- **Click on buttons** to enable/disable object detection for specific categories.
- **Scroll with the mouse wheel** to navigate the object selection panel.
- **Press `ESC`** to exit.

---

## 📜 **How It Works**
1. **Loads the YOLOv4-tiny model** via OpenCV’s `cv2.dnn_DetectionModel()`.
2. **Reads class labels** from `classes.txt`.
3. **Captures frames from the webcam** and processes them for detection.
4. **Detects objects** based on confidence threshold.
5. **Draws bounding boxes** and labels detected objects.
6. **Users can dynamically select objects** to detect via an interactive UI.

---

## 🎨 **UI Features**
- **Scrollable Button Panel** → All object categories fit neatly.
- **Compact Button Layout** → Easy readability & interaction.
- **Smooth Click & Scroll Support** → Optimized for usability.

### **Example Object Categories:**
| Object | Button Color |
|---------|-------------|
| Person | 🟦 Blue |
| Car | 🟥 Red |
| Dog | 🟩 Green |
| Bottle | 🟪 Purple |

---

## 🏗️ **How to Add More Object Categories?**
1. **Edit `dnn_model/classes.txt`**  
   - Add the new object name on a new line.
   
2. **Modify `initialize_buttons()` in `main4.py`**  
   - New buttons are automatically added using the categories list.
---

## 🚀 **Performance Optimization**
- Convert the model to **ONNX** for OpenCV acceleration:
  ```bash
  python export.py --weights best.pt --include onnx
  ```
- Run with **GPU acceleration** (if supported):
  ```python
  net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
  net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
  ```

---

## 📝 **TODOs & Future Improvements**
✔ Enhance UI further with dynamic styling  
✔ Add support for **YOLOv5**  
✔ Train a custom model for additional objects  
✔ Optimize for **edge devices** like Raspberry Pi  

---

## 📜 **License**
🔓 This project is open-source and available under the **MIT License**.

---

## 📬 **Contact & Support**
👨‍💻 **Maintainer**: [Reality361](https://github.com/Reality361)
💡 Have questions? Open an [issue](https://github.com/Reality361/opencv-object-detection-ui/issues).  
🚀 Enjoyed the project? Give it a ⭐ on GitHub!  
