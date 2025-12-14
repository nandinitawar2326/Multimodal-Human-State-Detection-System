# Multimodal-Human-State-Detection-System
A multimodal human state detection system that combines human activity recognition using smartphone sensors, voice emotion analysis using audio features, and face emotion detection using deep learning. The system fuses multiple modalities to infer overall human emotional and physical state in real time.
# Multimodal Human State Detection System

This project detects a person’s overall state by combining three modalities: 
Human Activity Recognition (HAR) using sensor data, Voice Emotion Detection 
using audio features, and Face Emotion Detection using a webcam. The system 
fuses all outputs to determine states like Calm, Happy, Sad, Angry, or High Energy.

## 🔧 Technologies Used
- Python 3.11
- Scikit-learn (Random Forest)
- Librosa (Audio Processing)
- DeepFace (Face Emotion)
- OpenCV
- NumPy, Pandas
- Tkinter (UI)

## 📂 Project Modules
- `har_train.py` – Train HAR model  
- `har_model.py` – Save trained HAR model  
- `voice_emotion.py` – Voice emotion detection  
- `face_emotion.py` – Face emotion detection using webcam  
- `multimodal_system.py` – Fusion logic  
- `multimodal_ui.py` – User Interface  

## ⚙️ How It Works
1. Detects body activity from sensor data  
2. Records and analyzes voice emotion  
3. Detects facial emotion via webcam  
4. Combines all results to predict final human state  

## 🎯 Applications
- Mental health monitoring  
- Smart surveillance  
- Human–Computer Interaction  
- Healthcare systems  

## 🚀 Future Scope
- Deep learning–based fusion  
- Mobile app integration  
- Cloud deployment  
- Real-time dashboards  


