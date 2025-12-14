import tkinter as tk
from voice_emotion import predict_voice_emotion
from face_emotion import predict_face_emotion

def detect_voice():
    result = predict_voice_emotion()
    voice_label.config(text=f"Voice Emotion: {result}")

def detect_face():
    result = predict_face_emotion()
    face_label.config(text=f"Face Emotion: {result}")

# -------- UI --------
root = tk.Tk()
root.title("Multimodal Emotion Detection")
root.geometry("400x300")

tk.Label(root, text="Human Emotion Detection", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Detect Voice Emotion", command=detect_voice).pack(pady=10)
voice_label = tk.Label(root, text="Voice Emotion: ---")
voice_label.pack()

tk.Button(root, text="Detect Face Emotion", command=detect_face).pack(pady=10)
face_label = tk.Label(root, text="Face Emotion: ---")
face_label.pack()

root.mainloop()
