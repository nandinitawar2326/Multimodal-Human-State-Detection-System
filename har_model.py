import os
import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

DATA_DIR = "sensor_data"
WINDOW_SIZE = 100
STEP_SIZE = 100

def extract_features(window):
    features = []
    for col in window.T:
        features.extend([
            col.mean(),
            col.std(),
            col.max(),
            col.min()
        ])
    return features

X, y = [], []

for file in os.listdir(DATA_DIR):
    if file.endswith(".csv"):
        label = file.split("_")[0]
        df = pd.read_csv(os.path.join(DATA_DIR, file))
        data = df.select_dtypes(include=[float, int]).iloc[:, :3].values

        for i in range(0, len(data) - WINDOW_SIZE, STEP_SIZE):
            window = data[i:i+WINDOW_SIZE]
            X.append(extract_features(window))
            y.append(label)

X = np.array(X)
y = np.array(y)

le = LabelEncoder()
y_enc = le.fit_transform(y)

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X, y_enc)

joblib.dump(model, "har_rf_model.pkl")
joblib.dump(le, "har_labels.pkl")

print("HAR model saved successfully")
