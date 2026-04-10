# 🧠 AI-Based Smart Exam Hall Monitoring System

## 🚀 Overview

This project implements a **real-time AI-powered monitoring system** designed for **exam hall surveillance**. It uses **computer vision (OpenCV + Haar Cascade)** to detect the presence of a student’s face and identify **suspicious behavior** when the face is missing for a defined duration.

The system provides:

* 🚨 Real-time alerts
* 🔊 Audio warning (beep)
* 📸 Automatic screenshot capture

---

## 🎯 Key Features

* 🎥 **Real-Time Webcam Monitoring**
* 👤 **Face Detection using Haar Cascade**
* 🚨 **Suspicious Activity Detection**

  * Detects when face is missing continuously
* 🔊 **Alert System**

  * Audible beep on detection
* 📸 **Automatic Screenshot Capture**
* ⚡ **Optimized Performance**

  * Fast camera initialization (DirectShow)
* 📊 **Live Status Display**

  * Face count + system status

---

## 🧠 How It Works

### 1. Face Detection

* Uses **Haar Cascade classifier**
* Detects frontal faces in grayscale frames

### 2. Behavior Tracking Logic

* Tracks consecutive frames with **no face detected**
* If threshold exceeded → marks as suspicious

### 3. Suspicious Detection Pipeline

* Missing face → Increment counter
* Threshold reached → Trigger alert
* Confirm suspicious state

### 4. Alert System

* 🔊 Beep sound using `winsound`
* 📸 Screenshot saved with timestamp
* 🚨 Visual alert banner on screen

---

## ⚙️ Tech Stack

* **Python 3**
* **OpenCV (cv2)**
* **Haar Cascade Classifier**
* **Winsound (Windows alert system)**
* **Time module**

---

## 📂 Project Structure

```id="p2c4z1"
📦 AI-Exam-Monitoring
 ┣ 📜 main.py
 ┣ 📜 haarcascade_frontalface_default.xml
 ┣ 📜 README.md
 ┗ 📜 screenshots/
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash id="k9d7xa"
git clone https://github.com/your-username/ai-exam-monitoring.git
cd ai-exam-monitoring
```

### 2. Install Dependencies

```bash id="8a1gdf"
pip install opencv-python
```

### 3. Run the Application

```bash id="z7k1op"
python main.py
```

---

## 📊 Configuration Parameters

| Parameter                 | Description                           |
| ------------------------- | ------------------------------------- |
| MISSING_FACE_THRESHOLD    | Frames before marking suspicious      |
| SUSPICIOUS_CONFIRM_FRAMES | Frames to confirm suspicious activity |
| BEEP_COOLDOWN             | Delay between alert sounds            |
| SCREENSHOT_DELAY          | Delay between screenshots             |

---

## 🚨 Detection Logic Summary

| Condition                 | Output        |
| ------------------------- | ------------- |
| Face detected             | ✅ Normal      |
| Face missing briefly      | ⚠️ Monitoring |
| Face missing continuously | 🚨 Suspicious |

---

## 📸 Output

* Live webcam feed
* Face bounding box (green)
* Alert banner (red)
* Saved screenshots of suspicious activity

---

## 🧠 Use Cases

* Exam Hall Monitoring Systems
* Online Proctoring
* Security Surveillance
* Attention Tracking Systems

---

## 🚀 Future Enhancements

* 🎯 Multi-face tracking
* 🤖 Deep learning face recognition
* 📡 Cloud alert system (SMS / Email)
* 📊 Behavior analytics dashboard
* 🌐 Web-based monitoring system

---

## 👨‍💻 Author

**Chandra Prakash**

---

## ⭐ Contribution

Feel free to fork, improve, and submit pull requests.

---

## 📜 License

This project is open-source under the MIT License.
