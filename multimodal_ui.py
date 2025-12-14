import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

from har_predict import predict_activity
from voice_emotion import predict_voice_emotion
from face_emotion import predict_face_emotion

# -------- GLOBAL STORAGE --------
activity = None
voice_emotion = None
face_emotion = None

# -------- FUNCTIONS --------
def detect_activity():
    global activity
    activity = predict_activity()
    lbl_activity.config(text=f"Activity: {activity}")

def detect_voice():
    global voice_emotion
    voice_emotion = predict_voice_emotion()
    lbl_voice.config(text=f"Voice Emotion: {voice_emotion}")

def detect_face():
    global face_emotion
    face_emotion = predict_face_emotion()
    lbl_face.config(text=f"Face Emotion: {face_emotion}")

def show_final_state():
    if not (activity and voice_emotion and face_emotion):
        messagebox.showwarning("Incomplete", "Please detect Activity, Voice and Face first")
        return

    # -------- FUSION LOGIC (UNCHANGED) --------
    if "angry" in [voice_emotion, face_emotion]:
        state = "Angry / Stressed"
    elif voice_emotion == face_emotion == "happy":
        state = "Happy"
    elif voice_emotion == face_emotion == "sad":
        state = "Sad"
    elif voice_emotion == "calm" and activity in ["sitting", "standing"]:
        state = "Calm & Relaxed"
    else:
        state = "Neutral"

    lbl_final.config(text=f"FINAL HUMAN STATE:\n{state}")

    # show face image
    img = Image.open("final_face.jpg")
    img = img.resize((220, 220))
    photo = ImageTk.PhotoImage(img)
    lbl_image.config(image=photo)
    lbl_image.image = photo

# -------- UI --------
root = tk.Tk()
root.title("Multimodal Human State System")
root.geometry("520x720")
root.configure(bg="#1e1e2f")

title = tk.Label(root, text="Multimodal Human State Detection",
                 font=("Arial", 18, "bold"), fg="white", bg="#1e1e2f")
title.pack(pady=15)

btn_style = {
    "font": ("Arial", 12, "bold"),
    "width": 25,
    "height": 2,
    "bg": "#4CAF50",
    "fg": "white"
}

tk.Button(root, text="Detect Activity", command=detect_activity, **btn_style).pack(pady=8)
lbl_activity = tk.Label(root, text="Activity: --", fg="white", bg="#1e1e2f")
lbl_activity.pack()

tk.Button(root, text="Detect Voice Emotion", command=detect_voice, **btn_style).pack(pady=8)
lbl_voice = tk.Label(root, text="Voice Emotion: --", fg="white", bg="#1e1e2f")
lbl_voice.pack()

tk.Button(root, text="Detect Face Emotion", command=detect_face, **btn_style).pack(pady=8)
lbl_face = tk.Label(root, text="Face Emotion: --", fg="white", bg="#1e1e2f")
lbl_face.pack()

tk.Button(root, text="SHOW FINAL HUMAN STATE", command=show_final_state,
          bg="#FF9800", fg="white", font=("Arial", 13, "bold"),
          width=28, height=2).pack(pady=20)

lbl_final = tk.Label(root, text="", font=("Arial", 14, "bold"),
                     fg="#00FFAA", bg="#1e1e2f")
lbl_final.pack(pady=10)

lbl_image = tk.Label(root, bg="#1e1e2f")
lbl_image.pack(pady=10)

root.mainloop()
