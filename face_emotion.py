import cv2
from deepface import DeepFace

def predict_face_emotion():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    result = DeepFace.analyze(
        frame,
        actions=['emotion'],
        enforce_detection=False
    )

    emotion = result[0]['dominant_emotion']

    # Save face image
    cv2.imwrite("face.jpg", frame)

    return emotion, "face.jpg"
def predict_face_emotion():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    result = DeepFace.analyze(
        frame,
        actions=['emotion'],
        enforce_detection=False
    )

    emotion = result[0]['dominant_emotion']
    cv2.imwrite("last_face.jpg", frame)
    return emotion
import cv2
from deepface import DeepFace

def predict_face_emotion():
    cap = cv2.VideoCapture(0)
    emotion = "unknown"
    frame_captured = None

    print("Opening webcam... Press SPACE to capture face")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Face Emotion - Press SPACE", frame)

        key = cv2.waitKey(1)
        if key == 32:  # SPACE
            frame_captured = frame.copy()
            result = DeepFace.analyze(
                frame,
                actions=['emotion'],
                enforce_detection=False
            )
            emotion = result[0]['dominant_emotion']
            break

    cap.release()
    cv2.destroyAllWindows()

    if frame_captured is not None:
        cv2.imwrite("final_face.jpg", frame_captured)

    return emotion
