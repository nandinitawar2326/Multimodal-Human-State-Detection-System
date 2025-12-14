import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# ---------- PARAMETERS ----------
DATA_DIR = "sensor_data"
WINDOW_SIZE = 100      # number of samples per window (~2 sec if 50 Hz)
STEP_SIZE = 100        # no overlap

# ---------- FEATURE FUNCTION ----------
def extract_features(window):
    features = []
    for col in window.T:   # ax, ay, az
        features.append(col.mean())
        features.append(col.std())
        features.append(col.max())
        features.append(col.min())
    return features

# ---------- LOAD DATA ----------
X = []
y = []

for file in os.listdir(DATA_DIR):
    if file.endswith(".csv"):
        label = "_".join(file.replace(".csv", "").split("_")[:-1])
   # standing / walking etc.
        df = pd.read_csv(os.path.join(DATA_DIR, file))

        # auto-detect acceleration columns
        cols = [c for c in df.columns if c.lower() in ['ax','ay','az']]
        if len(cols) < 3:
            cols = df.select_dtypes(include=[float, int]).columns[:3]

        data = df[cols].values

        # sliding windows
        for i in range(0, len(data) - WINDOW_SIZE, STEP_SIZE):
            window = data[i:i+WINDOW_SIZE]
            features = extract_features(window)
            X.append(features)
            y.append(label)

# ---------- ML PREP ----------
X = np.array(X)
y = np.array(y)

le = LabelEncoder()
y_encoded = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# ---------- TRAIN MODEL ----------
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print("HAR Model Accuracy:", accuracy)

print("Classes:", le.classes_)
