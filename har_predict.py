import joblib
import numpy as np
import pandas as pd

model = joblib.load("har_rf_model.pkl")
labels = joblib.load("har_labels.pkl")

def predict_activity():
    df = pd.read_csv("sensor_data/standing_01.csv")
    data = df.select_dtypes(include=[float, int]).iloc[:100, :3].values

    features = []
    for col in data.T:
        features.extend([col.mean(), col.std(), col.max(), col.min()])

    pred = model.predict([features])[0]
    return labels.inverse_transform([pred])[0]
